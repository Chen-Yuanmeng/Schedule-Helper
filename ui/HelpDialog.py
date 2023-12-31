import wx
import wx.html2
import ui.MyFrame


class HelpDialog(ui.MyFrame.MyFrame):
    def __init__(self, html_string):
        super().__init__('帮助', 600, 1000)

        self.Centre()

        # 浏览器控件
        if wx.html2.WebView.IsBackendAvailable(wx.html2.WebViewBackendEdge):  # Windows 10 +
            backend_to_use = wx.html2.WebViewBackendEdge
        elif wx.html2.WebView.IsBackendAvailable(wx.html2.WebViewBackendWebKit):  # GTK/GTK3/macOS
            backend_to_use = wx.html2.WebViewBackendWebKit
        elif wx.html2.WebView.IsBackendAvailable(wx.html2.WebViewBackendIE):  # Windows 7 +
            backend_to_use = wx.html2.WebViewBackendIE
        else:
            backend_to_use = wx.html2.WebViewBackendDefault  # 默认
        self.help_text: wx.html2.WebView = wx.html2.WebView.New(self, backend=backend_to_use)
        self.help_text.SetSize(self.GetVirtualSize())
        self.help_text.SetPage(html_string, '')

        self.Show()

        self.Bind(wx.EVT_CLOSE, self.close)
        self.Bind(wx.EVT_SIZE, self.on_size)

    def close(self, _):
        self.Destroy()

    def on_size(self, _):
        self.help_text.SetSize(self.GetVirtualSize())
