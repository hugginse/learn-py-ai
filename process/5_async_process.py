import multiprocessing
import time

def task(x):
    time.sleep(0.5)
    return x * 10


if __name__ == '__main__':
    with multiprocessing.Pool(processes=3) as pool:
        tasks = []
        for i in range(5):
            # 异步提交任务
            async_res = pool.apply_async(task, args=(i,))
            # 将异步结果对象存入列表
            tasks.append(async_res)

        # 统一获取所有任务的结果
        final_results = [res.get() for res in tasks]
    print(f"所有任务完成, 结果为: {final_results}")