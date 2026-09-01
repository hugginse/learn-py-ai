import multiprocessing
import time 

def heavy_calc(n):
    s = 0
    for i in range(n):
        s += i ** 3
    return s

if __name__ == '__main__':
    task_data = [10000000] * 8

    # 单进程串行执行
    start_time = time.time()
    for data in task_data:
        heavy_calc(data)
    print(f"单进程串行执行耗时: {time.time() - start_time:.2f}秒")

    # 多进程并行执行
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(heavy_calc, task_data)
    print(f"多进程并行执行耗时: {time.time() - start_time:.2f}秒")