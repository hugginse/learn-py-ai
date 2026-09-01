import multiprocessing 
import time 

class MyPorcess(multiprocessing.Process):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print(f"Task {self.name} starting...")
        time.sleep(self.delay)
        print(f"Task {self.name} completed after {self.delay} seconds.")

if __name__ == '__main__':
    print(f"main process id: {multiprocessing.current_process().pid}\n")
    # 创建子进程
    p1 = MyPorcess('A', 2)
    p1.start()
    p1.join()
    print("All tasks completed.")