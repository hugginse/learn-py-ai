import threading
import time

cond = threading.Condition()
goods = 0
max_goods = 5

# 生产者
def producer():
    global goods
    while True:
        with cond:
            if goods >= max_goods:
                print("仓库满，生产者等待")
                cond.wait()

            goods += 1
            print(f"生产1件，库存: {goods}")
            cond.notify_all() # 唤醒消费者
        time.sleep(0.5)

# 消费者
def consumer():
    global goods
    while True:
        with cond:
            if goods <= 0:
                print("仓库空，消费者等待")
                cond.wait()

            goods -= 1
            print(f"消费1件，库存: {goods}")
            cond.notify_all() # 唤醒生产者
        time.sleep(1)

t_p = threading.Thread(target=producer, daemon=True)
t_c = threading.Thread(target=consumer, daemon=True)
t_p.start()
t_c.start()
time.sleep(10)
print("程序结束")