# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from multiprocessing import Pool
import os, time, random

def long_time(name):
    print('Run Task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() *3)
    end = time.time()
    print('Task %s took %0.2f seconds' % (name, end - start))

if __name__ == '__main__':
    print('Task子进程 %s.' % os.getpid())
    p = Pool(5)
    for i in range(5):
        #apply_async() 异步提交任务到进程池的一个方法调用
        p.apply_async(long_time, args=(i,))
    print('Waiting for all subprocesses done...')
    #调用close() task 0，1，2，3是立刻执行的
    # join() 等待进程池中的所有子进程执行完毕。
    p.close()
    p.join()
    print('All subprocesses done.')

