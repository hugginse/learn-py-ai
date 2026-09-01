import threading

num = 0
lock = threading.Lock()     # 创建互斥锁

def add():
    global num
    for _ in range(100000):
        # 自动加锁， 代码结束后自动释放
        with lock:
            num += 1

if __name__ == "__main__":
    t1 = threading.Thread(target=add)
    t2 = threading.Thread(target=add)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"正确结果： ", num) #固定输出200000