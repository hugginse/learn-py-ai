import asyncio

# 异步队列：存放生产的数据，设置最大容量3
queue = asyncio.Queue(maxsize=3)

# 生产者协程
async def producer():
    for i in range(6):  # 一共生产6个商品
        item = f"商品-{i}"
        await queue.put(item)
        print(f"生产者：生产 {item}, 当前队列大小：{queue.qsize()}")
        await asyncio.sleep(0.5)

# 消费者协程
async def consumer():
    while True:
        # 队列为空时，协程阻塞等待数据
        item = await queue.get()
        print(f"消费者：消费 {item}, 当前队列大小：{queue.qsize()}")
        await asyncio.sleep(1) # 模拟消费耗时
        queue.task_done()   # 标记 一个任务消费完成

async def main():
    # 创建生产者、消费者任务
    prod_task = asyncio.create_task(producer())
    cons_task = asyncio.create_task(consumer())

    # 等待生产者全部生产完毕
    await prod_task
    # 等待队列立所有剩余商品全部被消费完
    await queue.join()
    # 取消无限循环的消费任务
    cons_task.cancel()

if __name__ == "__main__":
    asyncio.run(main())