from concurrent.futures import ThreadPoolExecutor
import time

def task(num):
    print(f"任务{num}开始")
    time.sleep(1)
    return f"任务{num}完成"

if __name__ == "__main__":
    # max_workers: 线程池最大并发数
    with ThreadPoolExecutor(max_workers=4) as pool:
        # 提交任务, 返回Future
        futures = [pool.submit(task, i) for i in range(6)]
        # 获取结果
        for f in futures:
            print(f.result())