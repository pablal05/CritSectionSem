#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:14:11 2022

@author: mat
"""
from multiprocessing import Process, Lock
from multiprocessing import current_process
from multiprocessing import Value, Array
N = 8


def task(tid, common, lock):
 a = 0
 for i in range(100):
     print(f"{tid}−{i}: Non−critical Section")
     a += 1
     print(f"{tid}−{i}: End of non−critical Section")
     lock.acquire()
     try:
         print(f"{tid}−{i}: Critical section")
         v = common.value + 1
         print(f"{tid}−{i}: Inside critical section")
         common.value = v
         print(f"{tid}−{i}: End of critical section")
     finally:
         lock.release()
     
def main():
 lp = []
 
 common = Value("i", 0)
 lock = Lock()
 
 for tid in range(N):
     lp.append(Process(target=task, args=(tid, common, lock)))
 print (f"Valor inicial del contador {common.value}")
 for p in lp:
     p.start()
 for p in lp:
     p.join()
 print (f"Valor final del contador {common.value}")
 print ("fin")
 
if __name__ == "__main__":
    main()
 

