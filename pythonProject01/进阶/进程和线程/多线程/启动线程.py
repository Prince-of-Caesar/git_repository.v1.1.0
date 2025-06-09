# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
# threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name = 'LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程 MainThread，
# 主线程又可以启动新的线程,我们用LoopThread命名子线程
# 如果不起名字Python就自动给线程命名为Thread-1，Thread-2……