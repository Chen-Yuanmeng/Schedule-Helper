import wx
from DisplayConfig import DISPLAY_SCALE


class MyFrame(wx.Frame):
    def __init__(self, title, width=0, height=0, parent=None, id=-1, style=wx.DEFAULT_FRAME_STYLE):
        if width == 0 or height == 0:
            super().__init__(parent, id, title, size=wx.DefaultSize, style=style)
        else:
            super().__init__(parent, id, title, size=(width * DISPLAY_SCALE, height * DISPLAY_SCALE), style=style)
        self.panel = wx.Panel(self)
        ico = wx.Icon('../assets/ScheduleHelper.ico')
        self.SetIcon(ico)
