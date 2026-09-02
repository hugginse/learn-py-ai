def outer():
    num = 100

    def inner():
        print(num)
    return inner
fn = outer()
# 查看自由变量名
print(fn.__code__.co_freevars)
# 查看闭包保存的变量对象
print(fn.__closure__)