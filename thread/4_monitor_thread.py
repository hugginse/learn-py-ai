import threading
import time

def test():
    time.sleep(2)

t = threading.Thread(target=test)
print(f"启动前是否活跃: ", t.is_alive())
t.start()
print(f"启动后是否活跃: ", t.is_alive())
print(f"当前线程名: ", threading.current_thread().name)
print(f"活跃线程数量: ", threading.active_count())
t.join()
print(f"结束后是否活跃: ", t.is_alive())