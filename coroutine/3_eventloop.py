import asyncio
import time

async def sleep_demo():
    print("开始异步等待2秒模拟IO阻塞")
    # 异步休眠: 替代同步time.sleep(), 不会卡死线程
    await asyncio.sleep(2)
    print("2秒IO等待结束，恢复协程执行")

def dm01():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sleep_demo())
    loop.close()

async def task(name, delay):
    print(f"任务{name} 启动, 需要等待 {delay}")
    await asyncio.sleep(delay)
    print(f"任务{name} 执行完毕")
    return f"{name} 执行结果"

async def main():
    start_time = time.time()
    # 创建两个任务，并发执行，此刻没有执行
    t1 = asyncio.create_task(task("A", 5))
    t2 = asyncio.create_task(task("B", 2))

    # 主线程等待两个任务全部执行结束，接收返回值
    # 起始在这里才算做等待执行，主协程main让出cpu控制权，事件循环调度其他协程
    res1 = await t1
    res2 = await t2

    total_time = time.time() - start_time
    print(f"\n总耗时： {total_time:.2f} s")
    print(res1, res2)

def dm02():
    asyncio.run(main())
    
if __name__ == "__main__":
    # dm01()
    dm02()