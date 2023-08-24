#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 05:57:05 2017
@author: bethanygarcia
 
NOTE:  timeit tests were run on an decrepit core duo Macbook Pro, 
       so your times will be faster than mine.
"""
#This is a single generator comprehension and is way less readable IMHO.
#It's also the SLOWEST by a factor of 50 or more.  ~222ms!!
def primes_III(number):
    primes = (item for item in range(2, number+1) if item not in
             (not_prime for item in range(2, number+1) for
              not_prime in range(item*item, number+1, item)))
    
    return list(primes)
#My first 'longhand' solution - I *hate* the nested looping here
#Not bad, but not great.  ~18.7ms
def primes_II(number):
    not_prime = []
    prime = []
    
    for item in range(2, number+1):
        if item not in not_prime:
            prime.append(item) 
            for element in range (item*item, number+1, item):
                not_prime.append(element)
    
    return prime
               
#Using set math. Pretty darn good - but it's still over
#4x slower than the fastest solution!   ~1.7ms
def primes_I(number):
    numbers = set(item for item in range(2, number+1))
    
    not_prime = set(not_prime for item in range(2, number+1)
                    for not_prime in range(item**2, number+1, item))
    
    #sorting adds .2ms, but the tests won't pass with an unsorted list
    return  sorted(list((numbers - not_prime)))
#Fastest by FAR - THANK YOU  @N-Parsons for the awesome solution.
#   ~405 usecs!!!
def primes(number):
    not_prime = set()
    primes = []
    for num in range(2, number+1):
        if num not in not_prime:
            primes.append(num)
            not_prime.update(range (num*num, number+1, num))
    return primes


if __name__ == '__main__':
    import time
    LIMIT = 10_000_000
    start_time = time.time()
    primes(LIMIT)
    end_time = time.time()
    print(f"Primes     time: {end_time - start_time}")
    # start_time = time.time()
    # primes_I(LIMIT)
    # end_time = time.time()
    # print(f"Primes_I   time: {end_time - start_time}")
    # start_time = time.time()
    # primes_II(LIMIT)
    # end_time = time.time()
    # print(f"Primes_II  time: {end_time - start_time}")
    # start_time = time.time()
    # primes_III(LIMIT)
    # end_time = time.time()
    # print(f"Primes_III time: {end_time - start_time}")
    