#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:52:04 2018

@author: simon
"""

n = 1

b_cnt = 0

def isbouncy(n):
    dig_num = len(str(n))
    if dig_num <= 2:
        return False
    str_num = str(n)
    prev_char = ''
    isInc = True
    isDec = True
    for x in range(1, len(str_num)):
        prev_char = int(str_num[x-1])
        cur_char = int(str_num[x])
        if prev_char > cur_char:
            isInc = False
        if prev_char < cur_char:
            isDec = False
    if (isInc==False) and (isDec==False):
        return True
    else:
        return False

# Various unit tests

assert isbouncy(134468) == False
assert isbouncy(66420) == False
assert isbouncy(155349) == True

while (True) and (n<=1000):
    if isbouncy(n):
        b_cnt += 1
    if (b_cnt/n)==0.99:
        break
    n += 1

assert b_cnt == 525

b_cnt = 0
n = 1

while (True):
    if isbouncy(n):
        b_cnt += 1
    if (b_cnt/n)==0.5:
        break
    n += 1

assert n == 538

b_cnt = 0
n = 1

while (True):
    if isbouncy(n):
        b_cnt += 1
    if (b_cnt/n)==0.90:
        break
    n += 1

assert n == 21780

# Actual running code

b_cnt = 0
n = 1

while (True):
    if isbouncy(n):
        b_cnt += 1
    if (b_cnt/n)==0.99:
        break
    n += 1

print(n)
