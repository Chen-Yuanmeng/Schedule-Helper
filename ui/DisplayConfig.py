import ctypes
from win32api import GetSystemMetrics

dip = GetSystemMetrics(0)

# 高分辨率DPI缩放问题设置
ctypes.windll.shcore.SetProcessDpiAwareness(1)

size = GetSystemMetrics(0)

DISPLAY_SCALE = size / dip

del size, dip
