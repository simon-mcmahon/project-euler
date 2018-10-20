#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:50:30 2018

@author: simon
"""

from math import sqrt, ceil, log10
from collections import defaultdict

def freq_dict(lst):
    digs = defaultdict(int)
    lst = str(lst)
    for j in lst:
        digs[int(j)] += 1
    return digs

#Generate the primes up to 1 million
max_num = 10**6
nums = range(2, max_num+1)
k=2
crossed_out = []
crossed_out.append(k)
while k <= sqrt(max_num):
    nums = list(filter(lambda x: (x%k!=0 or x==k),nums))
    crossed_out.append(k)
    for x in nums:
        if x in crossed_out:
            continue
        else:
            k=x
            break

primes = nums
print(len(primes))

prime_digs = [] # Split into bins for digits (in sets)
for dig in range(1, ceil(log10(max_num))+1):
    prime_dig = list(filter(lambda x: len(str(x))==dig, primes))
    prime_digs.append(set(prime_dig))

assert sum(map(lambda x: len(x), prime_digs)) == len(primes)

eight_sets = []

for dig_set in prime_digs:
    for num in dig_set:
        freq = freq_dict(num)
        if (freq[0]==0) and (freq[1]==0) and (freq[2]==0):
#            print('exit here')
            continue
        for j in [0,1,2]: # Get the series for each number
            if freq[j] == 0:
                continue
            subbed_list = list(map(lambda x: int(str(num).replace(str(j), str(x))), range(0, 10)))
            
            matched = []
            # See if the series is 8 long
            for series in subbed_list:
                if series in dig_set:
                    matched.append(series)
            if len(matched)==8:
                print(matched)
                eight_sets.append(matched)
                
