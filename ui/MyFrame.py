import wx
import ui.DisplayConfig


class MyFrame(wx.Frame):
    def __init__(self, title, width=0, height=0, parent=None, id=-1, style=wx.DEFAULT_FRAME_STYLE):
        if width == 0 or height == 0:
            super().__init__(parent, id, title, size=wx.DefaultSize, style=style)
        else:
            super().__init__(parent, id, title, size=(width * ui.DisplayConfig.DISPLAY_SCALE, height * ui.DisplayConfig.DISPLAY_SCALE), style=style)
        self.panel = wx.Panel(self)
        ico = wx.Icon('./assets/ScheduleHelper.ico')
        self.SetIcon(ico)
