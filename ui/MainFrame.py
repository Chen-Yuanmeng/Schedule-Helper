import wx
from os import system
from MyFrame import MyFrame
from MyFont import MyFont
from HelpDialog import HelpDialog
from DisplayConfig import DISPLAY_SCALE


class MainFrame(MyFrame):
    MENU_ID_EXIT = 101
    MENU_ID_HELP_DOCUMENTATION = 102
    MENU_ID_FEEDBACK = 103
    MENU_ID_REPORT = 104
    MENU_ID_GITHUB = 105
    MENU_ID_HOMEPAGE = 106
    MENU_ID_ABOUT = 107

    def __init__(self):
        super().__init__('课程表导入日历助手')

        # 字体
        self.font = MyFont(12, '微软雅黑')
        self.font_small = MyFont(11, '微软雅黑')

        # 整体sizer布局
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.step_1 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, 'Step 1: 设置课节')
        self.step_2 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, 'Step 2: 设置课程')
        self.step_3 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, 'Step 3: 设置提醒')
        self.step_4 = wx.StaticBoxSizer(wx.VERTICAL, self.panel, 'Step 4: 导出文件')

        # 顶部文字
        self.text = wx.StaticText(self.panel, -1, '下面，程序会引导你制作一份可以将你的课程表导入各\n大手机日历APP、邮箱日历的小工具')
        self.text.SetFont(self.font)

        # 第一个框
        self.text_1 = wx.StaticText(self.panel, -1, '首先，请打开文件夹中的“设置课节.xlsx”，并按\n提示操作')
        self.text_1.SetFont(self.font)
        self.button_1 = wx.Button(self.panel, -1, '然后，点击这个按钮导入课节', size=(350 * DISPLAY_SCALE, 45 * DISPLAY_SCALE))
        self.button_1.SetFont(self.font_small)
        self.button_1.Bind(wx.EVT_BUTTON, self.on_click_button_1)
        self.step_1.Add(self.text_1, 0, wx.ALL, 5)
        self.step_1.Add(self.button_1, 0, wx.ALL, 5)

        # 第二个框
        self.text_2 = wx.StaticText(self.panel, -1, '首先，请打开文件夹中的“设置课程.xlsx”，并按\n提示操作')
        self.text_2.SetFont(self.font)
        self.button_2 = wx.Button(self.panel, -1, '然后，点击这个按钮导入课程', size=(350 * DISPLAY_SCALE, 45 * DISPLAY_SCALE))
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
        self.button_4 = wx.Button(self.panel, -1, '生成ics文件')
        self.button_4.SetFont(self.font_small)
        self.button_4.Bind(wx.EVT_BUTTON, self.on_click_button_4)
        self.text_4_1 = wx.StaticText(self.panel, -1, '完成后，点击下面的按钮生成文件')
        self.text_4_1.SetFont(self.font)
        self.text_4_2 = wx.StaticText(self.panel, -1, '你可以将文件通过微信传到手机->用其他程序打开\n->选择日历APP，导入到你的日历中')
        self.text_4_2.SetFont(self.font)
        self.step_4.Add(self.text_4_1, 0, wx.ALL, 5)
        self.step_4.Add(self.button_4, 0, wx.ALL, 5)
        self.step_4.Add(self.text_4_2, 0, wx.ALL, 5)

        self.sizer.Add(self.text, 0, wx.ALL, 10)
        self.sizer.Add(self.step_1, 0, wx.ALL | wx.EXPAND, 10)
        self.sizer.Add(self.step_2, 0, wx.ALL | wx.EXPAND, 10)
        self.sizer.Add(self.step_3, 0, wx.ALL | wx.EXPAND, 10)
        self.sizer.Add(self.step_4, 0, wx.ALL | wx.EXPAND, 10)

        # 设置页面布局
        self.panel.SetSizerAndFit(self.sizer)
        self.sizer.SetSizeHints(self)

        # 添加菜单栏
        self.menu_bar = wx.MenuBar()

        self.file_menu = wx.Menu()
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

    def on_click_button_1(self, evt):
        ...

    def on_click_button_2(self, evt):
        ...

    def on_click_button_4(self, evt):
        ...

    def on_menubar(self, evt):
        id = evt.GetId()

        func_table = {self.MENU_ID_EXIT: self.on_exit,
            self.MENU_ID_HELP_DOCUMENTATION: self.on_open_doc,
            self.MENU_ID_FEEDBACK: self.on_feedback,
            self.MENU_ID_REPORT: self.on_report,
            self.MENU_ID_GITHUB: self.on_github,
            self.MENU_ID_HOMEPAGE: self.on_homepage,
            self.MENU_ID_ABOUT: self.on_about}

        func_table[id]()

    @staticmethod
    def on_exit():
        if wx.MessageBox('确认要退出程序吗？', '退出提示', wx.YES_NO | wx.NO_DEFAULT) == wx.YES:
            wx.Exit()

    @staticmethod
    def on_open_doc():
        with open('../docs/help.html', 'rb') as fp:
            if HelpDialog(fp.read()).ShowModal() == wx.ID_OK:
                ...   # 这里什么都不用写

    @staticmethod
    def on_feedback():
        system('start ') # 后接GitHub反馈地址

    @staticmethod
    def on_report():
        system('start ') # 后接GitHub反馈地址

    @staticmethod
    def on_github():
        system('start ') # 后接GitHub仓库地址

    @staticmethod
    def on_homepage():
        # 暂时还没写.io主页，这里先注释掉
        # system('start ')  # 后接GitHub反馈地址
        ...

    @staticmethod
    def on_about():
        wx.MessageBox('课程表导入日历助手\n\n本工具旨在帮助大学生方便管理自己的课程。\n\n本软件为开源，遵循地址', '关于软件')

