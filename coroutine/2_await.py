import asyncio

async def sleep_demo():
    print("开始异步等待2秒模拟IO阻塞")
    # 异步休眠: 替代同步time.sleep(), 不会卡死线程
    await asyncio.sleep(2)
    print("2秒IO等待结束，恢复协程执行")

# 启动事件循环，运行顶层协程
asyncio.run(sleep_demo())