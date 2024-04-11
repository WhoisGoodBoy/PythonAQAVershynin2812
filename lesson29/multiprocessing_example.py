from multiprocessing import Process, Queue, Pool, Lock


def f(x):
    print(f'hello, {x}')

def other_function(q):
    q.put([2,'dfhd',None])

def func_to_check_pool(x):
    return x*x

def func_to_check_lock(lock, x):
    lock.acquire()
    try:
        print(f'hello{x}')
    finally:
        lock.release()

if __name__ == '__main__':
    '''proc = Process(target=f, args=('Borys',))
    proc.start()
    proc.join()
    q = Queue()
    p = Process(target=other_function, args=(q,))
    p.start()
    print(q.get())
    p.join()
    
    with Pool(3) as pool:
        print(pool.map(func_to_check_pool, [1,2,3]))'''
    lock = Lock()
    for number in range(20):
        p = Process(target=func_to_check_lock, args=(lock,number))
        p.start()
