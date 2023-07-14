from multiprocessing import Process, Value, Array, Lock
import os
import time

#def square_number():
#    for i in range(1000):
#        i*i

time1=time.perf_counter()

def add_100(number,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        number.value+=1
        lock.release()


if __name__=="__main__":
    lock=Lock()
    shared_number= Value('i',0)
    print("Number at the begining is ",shared_number.value)

    pro1 = Process(target=add_100, args=(shared_number,lock))
    pro2 = Process(target=add_100, args=(shared_number,lock))
   
    pro1.start()
    pro2.start()
    
    pro1.join()
    pro2.join()

    time2=time.perf_counter()
    print("number at the end is",shared_number.value)
    time=time2-time1
    print("Time taken " , {time})