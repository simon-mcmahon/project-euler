#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# THERE CAN ONLY EVER BE AT MOST ONE 1 AS IF THERE WERE MORE, REPLACE ALL BUT 
# 1 OF THE ONES WITH ZEROES AND REDUCE THE OVERALL NUMBER

"""
Created on Sat Oct  6 11:46:01 2018

@author: simon
"""
# OLD CODE
#------------------------

from math import factorial

fact_dict = {x: factorial(x) for x in range(0,10)}

f_vals = {}
sf_vals= {}
g_vals = {}
sg_vals = {}
def f(n):
    try:
        return f_vals[n]
    except KeyError:
        total = 0
        for char in str(n):
            total += fact_dict[int(char)]
        f_vals.update({n: total})
        return total


def sf(n):
    try:
        return sf_vals[n]
    except KeyError:
        total = 0
        num = f(n)
        for char in str(num):
            total += int(char)
        sf_vals.update({n:total})
        return total
    
def g(i):
    try:
        return g_vals[i]
    except KeyError:
        # Iterate over the memoized answers for sf first
        for num, key in enumerate(sf_vals):
            if num+1 != key:
                raise ValueError('dict elements out of order')
            elif sf_vals[key]==i:
                g_vals.update({i:key})
                return key
        # If not iterate over starting from the largest of the keys
        if len(sf_vals) > 0:
            count = max(sf_vals.keys())
        else:
            count = 1
        while True:
            if sf(count)==i:
                break
            count += 1
        g_vals.update({i:count})
        return count

def sg(i):
    try:
        return sg_vals[i]
    except KeyError:
        total = 0
        num = g(i)
        for char in str(num):
            total += int(char)
        sg_vals.update({i:total})
        return total

#------------------------

from math import factorial, ceil
from collections import defaultdict
import pandas as pd

def ds(n):
    total = 0
    for char in str(n):
        total += int(char)
    return total

unique_freq_digs = []

for fact_num in range(0,10):
    k = factorial(fact_num)
    max_len = 30
    periods= []
    periods_rev = []
    for mod9 in range(0,8):
        numbers = list(map(lambda x: 9*x + mod9, range(0,max_len)))
        N = 5
        seenN = set()
        # Find the first (up to N) occurances of each number
        first_occurs = defaultdict(list)
        digsums = list(map(lambda x: ds(k*x), numbers))
        for index,digsum in enumerate(digsums):
            if digsum in seenN:
                continue
            if len(first_occurs[digsum]) < N:
                first_occurs[digsum].append((fact_num, mod9, numbers[index]))
                unique_freq_digs += [[fact_num, numbers[index], mod9, digsum, len(first_occurs[digsum])]]
            else:
                seenN.add(digsum)
columns = ['digit', 'freq', 'freq_mod9', 'ds', 'occ_num']
df = pd.DataFrame(unique_freq_digs, columns=columns)
uniques = df['ds'].unique()
lowest = df[df['occ_num']==1]

print('number of unique digit sums {}'.format(uniques.shape))
print(lowest.groupby('digit').count())

#import itertools


def subset_sum(n):
    # Generator which gives all the unique partitions up to sum n in order.
    
    p=[0]*n
    k=0
    p[k] = n
    
    while True:
        if len(p[0:k+1])<=10 and sum(p[0:k+1])==n:
            yield p[0:k+1]
        
        rem_val = 0
        while k>=0 and p[k]==1:
            rem_val += p[k]
            k -= 1
        
        if k<0:
            return
        
        p[k] = p[k] - 1
        rem_val += 1
        
        while rem_val > p[k]:
            p[k+1] = p[k]
            rem_val = rem_val - p[k]
            k += 1
        
        p[k+1] = rem_val
        k+=1
        


from itertools import permutations
from sympy.utilities.iterables import multiset_permutations

def print_num(lst):
    out_str = ''
    digs = ['0','1','2','3','4','5','6','7','8','9']
    if lst[0] != 0: # Number has zeroes in it
        index = 1
        while True: # Find first non zero entry
            if lst[index] != 0:
                break
            index += 1
        out_str += digs[index] + digs[0]*lst[0] # 'X00000'
        out_str += digs[index]*(lst[index]-1)
        loop_over = lst[index+1: ]
    else:
        loop_over = lst
    for num, freq in enumerate(loop_over):
        num_adj = num + (10-len(loop_over))
        out_str += digs[num_adj]*freq
        
    return int(out_str)

fact_dict = {x:factorial(x) for x in range(0,10)}

permitted_mins = {x: set(lowest[lowest['digit']==x].sort_values('freq')['freq']) for x in range(0,10)}

def carry_cnt(int1, int2):
    s1,s2=str(int1), str(int2)
    l1,l2=len(s1),len(s2)
    if l1<=l2:
        x,y=s1,s2
    else:
        x,y=s2,s1
    count=0
    l=len(y)
    for i,j in enumerate(x[::-1]):
        if int(y[l-1-i])+int(j)>9:
            count+=1
    return count




def helper(int1, int2):
    return ds(int1) + ds(int2) - 9*carry_cnt(int1, int2)

def gmod(seek_num):
    max_digs = 50
    curr_digs = 1
#    seek_num = 40
    sol_set = []
    exit_bool = False
    while True and curr_digs<=max_digs:
#        print(curr_digs)
        if exit_bool:
            break
        for comb in subset_sum(curr_digs):
#            print(comb)
            comb = comb + [0]*(10-len(comb))
    #        a = list(multiset_permutations(comb))
    #        print(len(a))
            for p in multiset_permutations(comb):
#                print(p)
#                print('mod9 = {}'.format((p[0]+p[1]+2*p[2]-3*(p[3]+p[4]+p[5]))%9))
                if p[1:]==[0]*9: # All zeros number
                    continue
#                elif sum(p) != curr_digs:
#                    continue
                elif ((p[0]+p[1]+2*p[2])%3 != seek_num%3):
                    continue
                elif (p[0]+p[1]+2*p[2]-3*(p[3]+p[4]-p[5]))%9 != seek_num%9:
                    # Mod 9 doesnt work
                    continue
                if curr_digs >= 20:
                    skip = False
                    for dig, freq in enumerate(p):
                        if freq not in permitted_mins[dig]:
                            skip = True
                            break
                    if skip:
                        continue
                else:
                    if ds(sum([p[x]*fact_dict[x] for x in range(0,10)]))==seek_num:
                        exit_bool = True
                        sol_set += [print_num(p)]
                    
#                print(p)
    #        # Add in zeroes if not available
    #        comb = comb + [0]*(10-len(comb))
    #        for p in permutations(comb):
    #            print(p)
        
        curr_digs += 1
        
    return min(sol_set)
#        break

#test = gmod(seek_num=40)
#print(test)
test = gmod(3)

for x in range(1,41):
    try:
        assert g(x) == gmod(x)
    except AssertionError:
        print('Error in equality at {}'.format(x))


# Pre generate then process on
# Too slow

candidate_sols = {x:set() for x in range(0,9)}

max_digs = 2
curr_digs = 1
sol_set = []
exit_bool = False
while True and curr_digs<=max_digs:
    print(curr_digs)
    if exit_bool:
        break
    for comb in subset_sum(curr_digs):
#            print(comb)
        comb = tuple(comb + [0]*(10-len(comb)))
#        a = list(multiset_permutations(comb))
#        print(len(a))
        for p in multiset_permutations(comb):
#                print(p)
#                print('mod9 = {}'.format((p[0]+p[1]+2*p[2]-3*(p[3]+p[4]+p[5]))%9))
            if p[1:]==[0]*9: # All zeros number
                continue
            mod9 = (p[0]+p[1]+2*p[2]-3*(p[3]+p[4]-p[5]))%9
            candidate_sols[mod9].add(tuple(p))
    
    curr_digs += 1

all_sols_count = 0
for x in candidate_sols:
    temp_len = len(candidate_sols[x])
    print('mod9 = {}, number of sols {}'.format(x, temp_len))
    all_sols_count += temp_len
print('all up, {} solutions'.format(all_sols_count))

# -------------------------------------------


# Processing through solution of the modular equation, not listing all combinations
# p[0] + p[1] + 2*p[2] == seen-num (mod 3)
#sol_set = (0,1,2)
#sols_p123 = {x:[] for x in sol_set}
#for seen_num in sol_set:
#    print('equal to {} mod3'.format(seen_num))
#    for p0 in sol_set:
#        for p1 in sol_set:
#            for p2 in sol_set:
#                if (p0+p1+2*p2)%3==seen_num:
#                    sols_p123[seen_num].append((p0,p1,p2))

sol_set = (0,1,2,3,4,5,6,7,8)
sols_p1to5 = {x:[] for x in sol_set}
for seen_num in sol_set:
    print('equal to {} mod9'.format(seen_num))
    for p0 in sol_set:
        for p1 in sol_set:
            for p2 in sol_set:
                for p3 in sol_set:
                    for p4 in sol_set:
                        for p5 in sol_set:
                            mod9 = (p0+p1+2*p2-3*(p3+p4-p5))%9
                            if mod9 == seen_num:
                                partial = 1*p0 + 1*p1 + 2*p2 + 6*p3 + 24*p4 + 120*p5
                                p_sum = sum([p0,p1,p2,p3,p4,p5])
                                sols_p1to5[seen_num].append((p0,p1,p2,p3,p4,p5, p_sum,partial))
              
# Sort the lists in order of frequency sum
for key in sols_p1to5:
    sols_p1to5[key] = sorted(sols_p1to5[key], key=lambda x: x[6])
       
all_sols_count = 0
for x in sols_p1to5:
    temp_len = len(sols_p1to5[x])
    print('mod9 = {}, number of sols {}'.format(x, temp_len))
    all_sols_count += temp_len
print('all up, {} solutions'.format(all_sols_count))

# next we pre-calculate the 789 tuples
sols_p6to9 = []
for p6 in permitted_mins[6]:
    for p7 in permitted_mins[7]:
        for p8 in permitted_mins[8]:
            for p9 in permitted_mins[9]:
                partial = 720*p6 + 5040*p7 + 40320*p8 + 362880*p9
                p_sum = sum([p6,p7,p8,p9])
                sols_p6to9.append((p6,p7,p8,p9,p_sum,partial))

sols_p6to9 = sorted(sols_p6to9, key=lambda x: x[4])

# After the exhaustion of the one solution set, the minimum we can increase by is 9


                    

#print('Periods of the first {} numbers congruent to {} mod 9. for factorial {}'.format(max_len, mod9, fact_num))
#print(periods)
#print('REVERSE Periods of the first {} numbers congruent to {} mod 9. for factorial {}'.format(max_len, mod9, fact_num))
#print(periods_rev)