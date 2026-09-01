import multiprocessing


def add_num(share_list, lock, num):
    '''
    向共享列表中添加数据
    :param share_list: 共享列表
    :param lock: 锁对象
    :param num: 需要添加的数据
    :return: None
    '''
    # 获取锁, 保证同一时间只有一个进程可以操作共享资源
    lock.acquire()
    try:
        share_list.append(num)
        print(f"进程 {multiprocessing.current_process().name} 添加了数据: {num}")
    finally:
        lock.release()

if __name__ == '__main__':
    # 创建管理器
    manager = multiprocessing.Manager()
    # 创建共享列表
    share_list = manager.list()
    # 创建锁对象
    lock = multiprocessing.Lock()
    # 存储创建的子进程, 将来主进程等待所有子进程完成
    p_list = []
    for i in range(10):
        p = multiprocessing.Process(target=add_num, args=(share_list, lock, i))
        p.start()
        p_list.append(p)

    # 等待所有子进程完成
    for p in p_list:
        p.join()
    print(f"所有任务完成, 共享列表数据为:", share_list)
