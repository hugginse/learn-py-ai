import asyncio

# 定义标准的协程函数
async def hello_coroutine():
    print("协程内部代码执行了")

# 调用协程函数：仅生成协程实例，无打印输出
coro = hello_coroutine()
print(type(coro)) # <class "coroutine">