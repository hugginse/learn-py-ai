'''
闭包基础演示
条件：
1. 函数嵌套
2. 内部函数使用外部函数的变量
3. 外部函数返回内部函数
'''

# 定义外部函数
def outer_func(num1):
    # 定义内部函数
    def inner_func(num2):
        # 使用外部函数的变量
        num = num1 + num2
        print(f"current value: {num}")

    # 返回内部函数
    return inner_func

# 调用外部函数，返回内层函数的地址
# fn 等价于 inner_func， 常驻内存
fn = outer_func(10)
# 调用闭包函数, 等价于 inner_func(20)
fn(20)