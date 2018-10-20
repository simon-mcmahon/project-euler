#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:25:05 2018

@author: simon
"""

# Check a seq periodic

from math import factorial, ceil

def guess_seq_len(seq):
    guess = 1
    max_len = ceil(len(seq) / 2)
    for x in range(2, max_len):
        if (seq[0:x] == seq[x:2*x]):
            if x < ceil(len(seq)/3):
                if (seq[x:2*x] == seq[2*x:3*x]):
                    return x
            else:
                continue
            return x
    return guess

def ds(n):
    total = 0
    for char in str(n):
        total += int(char)
    return total

#k = factorial(4)
#max_len = 10**4
#poss_period = list(map(lambda x: ds(k*x), range(1,max_len+1)))
#
#ans = guess_seq_len(poss_period)
#print(ans)
#ans1 = guess_seq_len(poss_period[::-1])
#print(ans1)

# Conclusion up to 100,000 values the factorial digit sums are not periodic

#---------------------------------------------------
#fact_num = 4
#k = factorial(fact_num)
#max_len = 10**3
#periods= []
#periods_rev = []
#for mod9 in range(0,8):
#    numbers = map(lambda x: 9*x + mod9, range(0,max_len))
#    poss_period = list(map(lambda x: ds(k*x), numbers))
#    periods.append(guess_seq_len(poss_period))
#    periods_rev.append(guess_seq_len(poss_period[::-1]))
#
#print('Periods of the first {} numbers congruent to {} mod 9. for factorial {}'.format(max_len, mod9, fact_num))
#print(periods)
#print('REVERSE Periods of the first {} numbers congruent to {} mod 9. for factorial {}'.format(max_len, mod9, fact_num))
#print(periods_rev)

# Not periodic, but have limited values all of which are the samevalue mod 9.


