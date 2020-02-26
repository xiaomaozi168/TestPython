import re

'''
测试pywin32
'''
from win32.win32gui import *
windows = []
def get_windows(hwnd,param):
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd): # 用来过滤
        windows.append(GetWindowText(hwnd))  # 获得窗口标题
EnumWindows(get_windows, 0)
for i in windows:
    print(i)


'''
正则表达式练习
'''
print("------------------------------------------------------")
print(re.S)
 




print("------------------------------------------------------")



print("hello world!")
def fn():
    try:
        print(10/0)
    except:
        print("出现异常！")
    else:
        print("这个执行了吗？")

fn()
print("继续执行！")
print("我继续试试看能提交吗？")