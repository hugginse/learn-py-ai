import multiprocessing
import time

def producer(queue):
    '''
    生产者函数，向队列中放入数据
    :param queue: 共享队列
    :return: None
    '''

    for i in range(10):
        queue.put(f"数据-{i}")
        print(f"生产者生产了数据-{i}")
        time.sleep(0.05)
    queue.put("end")
    print("生产者结束生产数据")

def consumer(queue):
    '''
    消费者函数，从队列中取出数据
    :param queue: 共享队列
    :return: None
    '''

    while True:
        # 队列为空则阻塞
        data = queue.get()
        print(f"消费者消费了{data}")
        time.sleep(0.1)
        if data == "end":
            break
    print("消费者结束消费数据")

if __name__ == '__main__':
    # 创建共享队列
    queue = multiprocessing.Queue()
    # 创建生产者进程
    p1 = multiprocessing.Process(target=producer, args=(queue,))
    # 创建消费者进程
    p2 = multiprocessing.Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("所有任务完成")
