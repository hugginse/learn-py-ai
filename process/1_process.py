import multiprocessing
import time

def task(name, delay):
    print(f"Task {name} starting...")
    time.sleep(delay)
    print(f"Task {name} completed after {delay} seconds.")

print(f"main process id: {multiprocessing.current_process().pid}\n"
      f"'__name__ = {__name__}\n')")

if __name__ == '__main__':
    print(f"main process id: {multiprocessing.current_process().pid}\n")
    # 创建子进程
    p1 = multiprocessing.Process(target=task, args=('A', 2))
    p2 = multiprocessing.Process(target=task, kwargs={
        "name": 'B', "delay": 3
    })

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("All tasks completed.")