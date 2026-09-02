'''
演示nonlocal关键字的使用
'''

def outer_func():
    num1 = 10
    def inner_func():
        # 赋值优先被当作定义
        num1 = 20
        print(f"inner func num1 is {num1}")

    inner_func()
    print(f"outer func num1 is {num1}")
    return inner_func

def outer_func2():
    num1 = 10
    def inner_func():
        # 可以声明nonlocal关键字，表示使用外层函数的变量
        # 通知解释器去外层查找num1
        nonlocal num1
        # 修改的是outer_func2内部的局部变量num1
        num1 = 20
        print(f"inner func num1 is {num1}")

    inner_func()
    print(f"outer func num1 is {num1}")
    return inner_func

def outer_func3():
    num1 = 10
    def inner_func():
        # 使用外层函数的num1
        nonlocal num1
        num1 += 20
        print(f"inner func num1 is {num1}")

    inner_func()
    print(f"outer func num1 is {num1}")
    return inner_func

if __name__ == "__main__":
    outer_func()
    print("===" * 10)
    outer_func2()
    print("===" * 10)
    outer_func3()