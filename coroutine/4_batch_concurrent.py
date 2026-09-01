import asyncio
import time

async def task(name, delay):
    print(f'任务{name} 启动, 需要等待 {delay} s')
    await asyncio.sleep(delay)
    print(f'任务{name} 执行完毕')
    return f'{name} 执行结果'

async def gather_main():
    start = time.time()
    # 打包所有协程，等待 他们都执行结束
    result_list = await asyncio.gather(
        task("A", 2),
        task("B", 3),
        task("C", 1),
    )
    print(f"所有任务返回结果：", result_list)
    print(f"总耗时： {time.time() - start:.2f} s")

async def async_seq_main():
    # 也可以不包裹成任务 直接等待协程执行结束
    t1 = task("C", 3)
    t2 = task("D", 5)
    # 相当于串行
    res3 = await t1
    res4 = await t2

# 启动事件循环，调用gather main协程
# asyncio.run(gather_main())
asyncio.run(async_seq_main())