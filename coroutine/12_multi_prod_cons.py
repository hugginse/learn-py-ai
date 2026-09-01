import asyncio

queue = asyncio.Queue(maxsize=4)

# 单个生产者逻辑
async def producer(name, total):
    for i in range(total):
        item = f"{name}-货品{i}"
        await queue.put(item)
        print(f"【{name}】产出：{item} | 队列： {queue.qsize()}")
        await asyncio.sleep(0.4)


# 单个消费者逻辑
async def consumer(name):
    while True:
        item = await queue.get()
        print(f"【{name}】取走：{item} | 队列：{{queue.qsize()}}")
        await asyncio.sleep(0.8)
        # 每放入1个元素，就会产生一个未标记计数
        # task_done就会将这个未标记的计数-1
        # 将来queue.join就可以阻塞等待所有计数标记
        queue.task_done()

# 定义异步函数main()
async def main():
    # 2个生产者，各生产4件产品
    producers = [
        asyncio.create_task(producer("工厂A", 4)),
        asyncio.create_task(producer("工厂B", 4))
    ]

    # 3个消费者，并行消费
    consumers = [asyncio.create_task(consumer(f"顾客{i}")) for i in range(3)]
    # 等待所有生产者完工
    await asyncio.gather(*producers)
    # 等待消费者消费完成队列
    await queue.join()
    # 关闭所有的消费者，因为消费者是死循环
    [c.cancel() for c in consumers]

if __name__ == "__main__":
    asyncio.run(main())