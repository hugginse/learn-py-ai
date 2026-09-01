import threading
import time

event = threading.Event()

def wait_task():
    print("子线程等待信号...")
    event.wait()    # 阻塞, 直到set()
    print("收到信号，开始执行 任务")

def sent_signal():
   time.sleep(3) 
   print("发送通知信号")
   event.set()


if __name__ == "__main__":
    t1 = threading.Thread(target=wait_task)
    t2 = threading.Thread(target=sent_signal)
    t1.start()
    t2.start()
    t1.join()
    t2.join()