import multiprocessing
import time 

def calc_power(num):
    '''
    模拟CPU密集型任务，计算num的平方
    :param num: 需要计算平方的数字
    :return: num**2
    '''
    res = num ** 2
    time.sleep(0.3)
    print(f"计算 {num} 的平方结果为: {res}")
    return res

if __name__ == '__main__':
    # 获取CPU核心数， 设置进程池的大小
    core_count = multiprocessing.cpu_count()
    print(f"CPU核心数: {core_count}")

    # 创建进程池, 进程数=CPU核心数
    with multiprocessing.Pool(processes=core_count) as pool:
        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # map 自动分配任务, 阻塞等待全部任务完成, 返回结果列表
        results = pool.map(calc_power, data_list)
    print(f"所有任务完成, 结果为: {results}")