# Process之间肯定是需要通信的，Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process,Queue
import os, time, random

#写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['a','b','c']:
        print('put %s to Queue...' % value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码：
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('read %s from Queue...' % value)

if __name__=='__main__':
    #父进程创建Queue并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    #启动子进程写入：
    pw.start()
    #启动子进程读取：
    pr.start()
    #等待pw执行结束
    pw.join()
    #如果pr是死循环，强行终止
    pr.terminate()
