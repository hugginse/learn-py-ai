import threading
import time

def task(name, delay):
    '''
    线程执行函数
    '''
    print(f"线程 {name} 启动, 休眠 {delay}s")
    time.sleep(delay)
    print(f"线程 {name} 执行 完毕")

if __name__ == "__main__":
    # 创建线程对象, target=执行函数 args=参数元组
    t1 = threading.Thread(target=task, args=("A", 2))
    t2 = threading.Thread(target=task, args=("B", 1))

    # 启动线程
    t1.start()
    t2.start()

    # join(): 主线程阻塞, 等待子线程执行完毕再往下走
    t1.join()
    t2.join()
    print(f"所有线程执行完毕, 主线程退出")