import threading

rlock = threading.RLock()

def func():
    rlock.acquire()
    print("第一次加锁")
    rlock.acquire()
    print("同一线程二次加锁，不会阻塞")
    rlock.release()
    rlock.release

t = threading.Thread(target=func)
t.start()
t.join