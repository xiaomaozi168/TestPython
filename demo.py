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
