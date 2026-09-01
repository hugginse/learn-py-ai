import asyncio

queue = asyncio.Queue(maxsize=4)

# 生产者：死循环永久生产，不再限制总量
async def producer(name: str):
    num = 0
    while True:
        item = f"{name}-货品{num}"
        await queue.put(item)
        print(f"【{name}】产出：{item} | 队列当前数量：{queue.qsize()}")
        num += 1
        await asyncio.sleep(0.4) # 生产间隔

# 消费者: 死循环持续消费
async def consumer(name: str):
    while True:
        item = await queue.get()
        print(f"        【{name}】取走:{item} | 队列剩余：{queue.qsize()}")
        await asyncio.sleep(0.8)    # 消费比生产慢，队列会逐步堆满
        queue.task_done()

async def main():
    # 2个永久生产者
    producers = [
        asyncio.create_task(producer("工厂A")),
        asyncio.create_task(producer("工厂B")),
    ]

    # 3个永久消费者
    consumers = [asyncio.create_task(consumer(f"顾客{i+ 1}")) for i in range(3)]

    try:
        # 整体程序最多运行8s就超时退出
        await asyncio.wait_for(asyncio.Future(), timeout=8)
    except asyncio.TimeoutError:
        print("\n============ 运行事件结束，准备停止所有任务 ============")
        
    # 取消所有生产者、消费者无限循环任务
    for task in producers + consumers:
        task.cancel()

    # 等待素有任务正常取消完毕
    await asyncio.gather(*producers, *consumers, return_exceptions=True)
    print("所有生产消费任务已全部终止")

if __name__ == "__main__":
    asyncio.run(main())