#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:08:53 2018

@author: chirag
"""

def Form_primes():
    """
    Returns a list of primes numbers upto 10 ** 4.5 (HARDCODED)
    - Sieve of Eratosthenes
    """
    up_lmt = int(10 ** 4.5) + 1
    status_arr = [True for i in range(up_lmt + 1)]
    status_arr[0] = status_arr[1] = False
    status_arr[2] = True
    primes = []
    
    i = 2
    while i ** 2 <= up_lmt:
        if status_arr[i] == True:
            for j in range(2 * i, up_lmt + 1, i):
                status_arr[j] = False
        i += 1
        
    for i in range(up_lmt + 1):
        if status_arr[i] == True:
            primes.append(i)

    return primes
    
def main():
    """
    - Segmented sieve
    """
    primes = Form_primes()
    
    tc = int(input())
    for test in range(tc):
        l, r = map(int, input().split())
        arr = [True for i in range(l, r + 1)]
        if l == 1:
            arr[0] = False
            
        for prime in primes:
            if prime ** 2 <= r:
                start = (l // prime) * prime
                if start == 0:
                    start = prime
                for i in range(start, r + 1, prime):
                    if i >= l:
                        arr[i - l] = False
                if start == prime and prime >= l:
                    arr[start - l] = True
            else:
                break
        
        for i in range(r - l + 1):
            if arr[i] == True:
                print(l + i)
        print()
                
if __name__ == "__main__":
    main()
