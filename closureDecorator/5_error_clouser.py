'''
闭包循环引用问题
'''

# error case
funcs = []
# i 是局部变量
for i in range(3):
    def inner():
        # 因为内部函数要使用变量i, 所以触发闭包机制
        # 将i打包成cell， 放入inner.__closure__中
        # 内部函数访问i其实是获取i的地址中的数据
        print(i)
    # 将函数存储到列表中
    funcs.append(inner)

# 全部输出2, 而非0, 1, 2
funcs[0]()
funcs[1]()
funcs[2]()


# correct case
funcs = []

# i 是局部变量
for i in range(3):
    def inner(num = i):
        print(num)
    funcs.append(inner)

funcs[0]()
funcs[1]()
funcs[2]()