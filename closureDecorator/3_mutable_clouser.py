def outer():
    # 可变对象列表
    data = [1, 2, 3]
    def inner():
        data.append(4)
        print(data)
    return inner

f = outer()
f()