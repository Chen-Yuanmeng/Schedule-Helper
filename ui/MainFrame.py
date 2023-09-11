import wx
from os import system
from datetime import datetime
import ui.MyFrame as MyFrame
import ui.MyFont as MyFont
import ui.HelpDialog as HelpDialog
import ui.RestoreExcel as RestoreExcel
import ui.DisplayConfig as DisplayConfig
import core.parse_arrangement
import core.parse_course
import core.course
import core.event
import core.parse_sect
import core.get_filename


class MainFrame(MyFrame.MyFrame):
    MENU_ID_EXIT = 101
    MENU_ID_HELP_DOCUMENTATION = 102
    MENU_ID_FEEDBACK = 103
    MENU_ID_REPORT = 104
    MENU_ID_GITHUB = 105
    MENU_ID_HOMEPAGE = 106
    MENU_ID_ABOUT = 107
    MENU_ID_RESTORE_EXCEL = 108

    def __init__(self):
        super().__init__('课程表导入日历助手')

        self.dct_arrangement: dict | None = None
        self.ls_courses: list | None = None

        # 字体
        self.font = MyFont.MyFont(12, '微软雅黑')
        self.font_small = MyFont.MyFont(11, '微软雅黑')

        # 整体sizer布局
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.step_1 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, 'Step 1: 设置课节')
        self.step_2 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, 'Step 2: 设置课程')
        self.step_3 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, 'Step 3: 设置提醒')
        self.step_4 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, 'Step 4: 设置起始日期')
        self.step_5 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, 'Step 5: 导出文件')

        # 顶部文字
        self.text = wx.StaticText(self.panel, -1, '下面，程序会引导你制作一份可以将你的课程表导入各\n大手机日历APP、邮箱日历的小工具')
        self.text.SetFont(self.font)

        # 第一个框
        self.text_1 = wx.StaticText(self.panel, -1, '首先，请打开文件夹中的“设置课节.xlsx”，并按\n提示操作')
        self.text_1.SetFont(self.font)
        self.button_1 = wx.Button(self.panel, -1, '然后，点击这个按钮导入课节', size=(350 * DisplayConfig.DISPLAY_SCALE, 45 * DisplayConfig.DISPLAY_SCALE))
        self.button_1.SetFont(self.font_small)
        self.button_1.Bind(wx.EVT_BUTTON, self.on_click_button_1)
        self.step_1.Add(self.text_1, 0, wx.ALL, 5)
        self.step_1.Add(self.button_1, 0, wx.ALL, 5)

        # 第二个框
        self.text_2 = wx.StaticText(self.panel, -1, '首先，请打开文件夹中的“设置课程.xlsx”，并按\n提示操作')
        self.text_2.SetFont(self.font)
        self.button_2 = wx.Button(self.panel, -1, '然后，点击这个按钮导入课程', size=(350 * DisplayConfig.DISPLAY_SCALE, 45 * DisplayConfig.DISPLAY_SCALE))
        self.button_2.SetFont(self.font_small)
        self.button_2.Bind(wx.EVT_BUTTON, self.on_click_button_2)
        self.step_2.Add(self.text_2, 0, wx.ALL, 5)
        self.step_2.Add(self.button_2, 0, wx.ALL, 5)

        # 第三个框
        self.text_3_1 = wx.StaticText(self.panel, -1, '你希望在课程开始前')
        self.text_3_1.SetFont(self.font)
        self.text_3_2 = wx.StaticText(self.panel, -1, '分钟（注：此空不填则不会设置提醒）')
        self.text_3_2.SetFont(self.font)
        self.text_3_3 = wx.StaticText(self.panel, -1, '收到手机的通知提醒。PS：建议这个时间设置为你\n从寝室赶到离你最远的教室的用时')
        self.text_3_3.SetFont(self.font)
        self.textbox = wx.TextCtrl(self.panel, -1, '', size=(50, 32))
        self.step_3.Add(self.text_3_1, 0, wx.ALL, 5)
        self.step_3_2 = wx.BoxSizer(wx.HORIZONTAL)
        self.step_3_2.Add(self.textbox, 0, wx.ALL, 5)
        self.step_3_2.Add(self.text_3_2, 0, wx.ALL, 5)
        self.step_3.Add(self.step_3_2, 0, 0, 0)
        self.step_3.Add(self.text_3_3, 0, wx.ALL, 5)

        # 第四个框
        self.text_4_1 = wx.StaticText(self.panel, -1, '这学期的第一周第一天的日期是')
        self.text_4_1.SetFont(self.font)
        self.text_4_2 = wx.StaticText(self.panel, -1, '年')
        self.text_4_2.SetFont(self.font)
        self.text_4_3 = wx.StaticText(self.panel, -1, '月')
        self.text_4_3.SetFont(self.font)
        self.text_4_4 = wx.StaticText(self.panel, -1, '日。')
        self.text_4_4.SetFont(self.font)
        self.textbox_year = wx.TextCtrl(self.panel, -1, '', size=(60, 32))
        self.textbox_month = wx.TextCtrl(self.panel, -1, '', size=(50, 32))
        self.textbox_day = wx.TextCtrl(self.panel, -1, '', size=(50, 32))
        self.step_4.Add(self.text_4_1, 0, wx.ALL, 5)
        self.step_4_2 = wx.BoxSizer(wx.HORIZONTAL)
        self.step_4_2.Add(self.textbox_year, 0, wx.ALL, 5)
        self.step_4_2.Add(self.text_4_2, 0, wx.ALL, 5)
        self.step_4_2.Add(self.textbox_month, 0, wx.ALL, 5)
        self.step_4_2.Add(self.text_4_3, 0, wx.ALL, 5)
        self.step_4_2.Add(self.textbox_day, 0, wx.ALL, 5)
        self.step_4_2.Add(self.text_4_4, 0, wx.ALL, 5)
        self.step_4.Add(self.step_4_2, 0, 0, 0)

        # 第五个框
        self.button_5 = wx.Button(self.panel, -1, '生成ics文件')
        self.button_5.SetFont(self.font_small)
        self.button_5.Bind(wx.EVT_BUTTON, self.on_click_button_4)
        self.text_5_1 = wx.StaticText(self.panel, -1, '完成后，点击下面的按钮生成文件')
        self.text_5_1.SetFont(self.font)
        self.text_5_2 = wx.StaticText(self.panel, -1, '你可以将文件通过微信传到手机->用其他程序打开\n->选择日历APP，导入到你的日历中')
        self.text_5_2.SetFont(self.font)
        self.step_5.Add(self.text_5_1, 0, wx.ALL, 5)
        self.step_5.Add(self.button_5, 0, wx.ALL, 5)
        self.step_5.Add(self.text_5_2, 0, wx.ALL, 5)

        self.sizer.Add(self.text, 0, wx.ALL, 10)
        self.sizer.Add(self.step_1, 0, wx.ALL | wx.EXPAND, 10)
        self.sizer.Add(self.step_2, 0, wx.ALL | wx.EXPAND, 10)
        self.sizer.Add(self.step_3, 0, wx.ALL | wx.EXPAND, 10)
        self.sizer.Add(self.step_4, 0, wx.ALL | wx.EXPAND, 10)
        self.sizer.Add(self.step_5, 0, wx.ALL | wx.EXPAND, 10)

        # 设置页面布局
        self.panel.SetSizerAndFit(self.sizer)
        self.sizer.SetSizeHints(self)

        # 添加菜单栏
        self.menu_bar = wx.MenuBar()

        self.file_menu = wx.Menu()
        self.file_menu.Append(wx.MenuItem(self.file_menu, self.MENU_ID_RESTORE_EXCEL, '恢复Excel模板(&R)'))
        self.file_menu.AppendSeparator()
        self.file_menu.Append(wx.MenuItem(self.file_menu, self.MENU_ID_EXIT, '退出(&E)'))
        self.help_menu = wx.Menu()
        self.help_menu.Append(wx.MenuItem(self.help_menu, self.MENU_ID_HELP_DOCUMENTATION, '打开帮助文档(&D)'))
        self.help_menu.AppendSeparator()
        self.help_menu.Append(wx.MenuItem(self.help_menu, self.MENU_ID_FEEDBACK, '提出反馈(&F)'))
        self.help_menu.Append(wx.MenuItem(self.help_menu, self.MENU_ID_REPORT, '报告问题(&R)'))
        self.help_menu.AppendSeparator()
        self.help_menu.Append(wx.MenuItem(self.help_menu, self.MENU_ID_GITHUB, '打开 Github 主页(&G)'))
        # self.help_menu.Append(wx.MenuItem(self.help_menu, self.MENU_ID_HOMEPAGE, '打开软件主页(&H)'))
        self.help_menu.AppendSeparator()
        self.help_menu.Append(wx.MenuItem(self.help_menu, self.MENU_ID_ABOUT, '关于(&A)'))

        self.menu_bar.Append(self.file_menu, '文件(&F)')
        self.menu_bar.Append(self.help_menu, '帮助(&H)')

        self.SetMenuBar(self.menu_bar)

        self.menu_bar.Bind(wx.EVT_MENU, self.on_menubar)

        # 显示页面
        self.Centre()
        self.Show()

    def on_click_button_1(self, _):
        try:
            self.dct_arrangement = core.parse_arrangement.parse_arrangement()
        except FileNotFoundError:
            wx.MessageBox('没有找到文件“设置课节.csv”，请检查一下！', '错误', style=wx.ICON_ERROR)
        else:
            if not self.dct_arrangement:
                wx.MessageBox('没有找到您输入的课节，请检查一下！', '错误', style=wx.ICON_ERROR)
            else:
                message = '已找到以下课节，请核对：\n\n'
                for i in self.dct_arrangement.keys():
                    message += str(i) + ':  ' + self.dct_arrangement[i][0] + ' ~ ' + self.dct_arrangement[i][1]
                    message += '\n'
                message += '\n如果有误，请修改文件后重新按下按钮'
                wx.MessageBox(message, '提示')

    def on_click_button_2(self, _):
        try:
            self.ls_courses = core.parse_course.parse_courses()
        except FileNotFoundError:
            wx.MessageBox('没有找到文件“设置课程.csv”，请检查一下！', '错误', style=wx.ICON_ERROR)
        else:
            if not self.ls_courses:
                wx.MessageBox('没有找到您输入的课程，请检查一下！', '错误', style=wx.ICON_ERROR)
            else:
                message = '已找到以下课程，请核对：\n\n'
                for i in self.ls_courses:
                    message += i[0] + ' ' + i[1]
                    message += '\n'
                message += '\n如果有误，请修改文件后重新按下按钮'
                wx.MessageBox(message, '提示')

    def on_click_button_4(self, _):
        # 先检查填完没有
        message = []
        if self.dct_arrangement is None:
            message.append('请点击第一个按钮导入课节！')
        if self.ls_courses is None:
            message.append('请点击第二个按钮导入课程！')
        try:
            if self.textbox.GetValue():
                alarm = int(self.textbox.GetValue())
                assert alarm >= 0
            else:
                alarm = None
        except (ValueError, AssertionError):
            message.append('请在提醒时间处输入正整数或0或不填')
        if self.textbox_year.GetValue() == '' or self.textbox_month.GetValue() == '' or self.textbox_day.GetValue() == '':
            message.append('请输入第四步中的日期')
        else:
            try:
                origin = datetime(int(self.textbox_year.GetValue()), int(self.textbox_month.GetValue()), int(self.textbox_day.GetValue()))
            except ValueError:
                message.append('请确保输入了正确的日期')
        if message:
            message.insert(0, '错误信息\n')
            message.append('\n请根据错误信息重新输入')
            wx.MessageBox('\n'.join(message), '错误', style=wx.ICON_ERROR)
            return
        sect_time = core.parse_sect.parse_sect(self.dct_arrangement)
        name = core.get_filename.get_filename()
        fp = open(name, 'w', encoding='UTF-8')  # 输出文件
        print('BEGIN:VCALENDAR', file=fp)
        for c in self.ls_courses:
            course = core.course.Course(c, alarm, origin)
            course.iterate(origin, sect_time, fp)
        print('END:VCALENDAR', file=fp)
        fp.close()
        wx.MessageBox('已生成' + name + '，可以用微信等分享到手机->用日历APP或其他软件打开并导入', '提示')

    def on_menubar(self, evt):
        func_table = {self.MENU_ID_EXIT: self.on_exit,
            self.MENU_ID_RESTORE_EXCEL: self.on_restore,
            self.MENU_ID_HELP_DOCUMENTATION: self.on_open_doc,
            self.MENU_ID_FEEDBACK: self.on_feedback,
            self.MENU_ID_REPORT: self.on_report,
            self.MENU_ID_GITHUB: self.on_github,
            self.MENU_ID_HOMEPAGE: self.on_homepage,
            self.MENU_ID_ABOUT: self.on_about}

        func_table[evt.GetId()]()

    @staticmethod
    def on_exit():
        if wx.MessageBox('确认要退出程序吗？', '退出提示', wx.YES_NO | wx.NO_DEFAULT) == wx.YES:
            wx.Exit()

    @staticmethod
    def on_restore():
        RestoreExcel.restore_excel()
        wx.MessageBox('已经恢复 设置课节.xlsx 和 设置课程.xlsx 两文件', '提示')

    @staticmethod
    def on_open_doc():
        with open('./docs/help.html', 'rb') as fp:
            HelpDialog.HelpDialog(fp.read())

    @staticmethod
    def on_feedback():
        system('start https://github.com/Chen-Yuanmeng/Schedule-Helper/issues/new?assignees=&labels=%E9%9C%80%E6%B1%82&projects=&template=02-featureRequest.yml')  # 后接GitHub Issues - advice地址

    @staticmethod
    def on_report():
        system('start https://github.com/Chen-Yuanmeng/Schedule-Helper/issues/new?assignees=&labels=BUG&projects=&template=01-bugReport.yml')  # 后接GitHub Issues - bug地址

    @staticmethod
    def on_github():
        system('start https://github.com/Chen-Yuanmeng/Schedule-Helper')  # 后接GitHub仓库地址

    @staticmethod
    def on_homepage():
        # 暂时还没写.io主页，这里先注释掉
        # system('start ')  # 后接GitHub反馈地址
        ...

    @staticmethod
    def on_about():
        wx.MessageBox('课程表导入日历助手\n\n本工具旨在帮助大学生方便地在手机上查看自己的课程。\n\n'
                      '本软件为开源，遵循Apache-2.0许可证，详见关于->查看许可证。\n\n'
                      '更多信息可查看我们的GitHub发布页，详见帮助->打开GitHub主页。\n\n'
                      '我们欢迎大家使用我们的小工具，如果你感觉不错的话，可以推荐给朋友，或在GitHub上给我们一颗Star，这会对我们有非常大的帮助', '关于软件')

