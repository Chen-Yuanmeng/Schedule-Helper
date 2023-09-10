import wx


class MyFont(wx.Font):
    def __init__(self, point_size, face_name='微软雅黑', underline=False,
                 family=wx.FONTFAMILY_DEFAULT, style=wx.FONTSTYLE_NORMAL,
                 weight=wx.FONTWEIGHT_NORMAL):
        super(MyFont, self).__init__(point_size, family, style, weight, underline=underline,
                         faceName=face_name)
