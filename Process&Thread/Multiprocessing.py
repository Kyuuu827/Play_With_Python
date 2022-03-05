import time
import multiprocessing

#not multiprocessing
start = time.time()

def count(group):
    for i in range(1, 50001):
        print(f'{group} : {i}')

num_list = ['n1', 'n2', 'n3', 'n4']

for num in num_list:
    count(num)

print(f'{time.time()-start} s')


#multiprocessing - Process 함수 사용
start = time.time()

def count(group):
    for i in range(1, 50001):
        print(f'{group} : {i}')

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=count, args=('pr1',))
    process2 = multiprocessing.Process(target=count, args=('pr2',))
    process3 = multiprocessing.Process(target=count, args=('pr3',))
    process4 = multiprocessing.Process(target=count, args=('pr4',))

    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print(f'{time.time()-start} s')


#multiprocessing - Pool 함수 사용
start = time.time()

def count(group):
    for i in range(1, 50001):
        print(f'{group} : {i}')

num_list = ['n1', 'n2', 'n3', 'n4']

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    pool.map(count, num_list)
    pool.close()
    pool.join()

print(f'{time.time()-start} s')