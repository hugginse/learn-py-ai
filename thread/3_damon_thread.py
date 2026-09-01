import threading
import time

def daemon_task():
    while True:
        print(f"守护线程运行中...")
        time.sleep(1)


def normal_task():
    time.sleep(3)
    print(f"普通子线程结束")

if __name__ == "__main__":
    t1 = threading.Thread(target=daemon_task, daemon=True)
    t2 = threading.Thread(target=normal_task)

    t1.start()
    t2.start()

    t2.join()       # 等待普通线程3s结束
    print(f"主线程执行完毕, 守护线程直接销毁")