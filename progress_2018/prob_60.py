#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:14:34 2018

@author: simon
"""
from math import sqrt, floor
from collections import defaultdict

max_num = 10**8
# Load in the first primes up to a certain maximum value
primes = set()
with open('./primes/2T_part1.txt', 'r') as prime_file:
    local_max = 2
    line = prime_file.readline()
    while local_max <= max_num:
        num_list = list(map(lambda x: int(x), line.split('\t')))
        primes.update(num_list)
        local_max = num_list[-1] # max in list if last as sorted
        line = prime_file.readline()

valid_tuples = set()
count = 0
length = len(primes)
# Get the pairs of the
for prime in primes:
    count += 1
    if count % 1000 ==0:
        print(count)
    for j in range(0,len(str(prime))-1):
        first_num = int(str(prime)[0:j+1])
        second_num = int(str(prime)[j+1:])
        if (first_num not in primes) or (second_num not in primes):
            continue
        
        ordered_tuple = tuple(sorted([first_num, second_num]))
        
        if ordered_tuple in valid_tuples:
            continue
#        print('{}, {}'.format(first_num, second_num))
        if len(str(first_num))+len(str(second_num))!= len(str(prime)): 
            # zero in number case
            continue
        
        if int(str(second_num) + str(first_num)) in primes:
            valid_tuples.add(ordered_tuple)


print(valid_tuples)
# Run frequency on the graphed vertices
freq= defaultdict(int)
for tup in valid_tuples:
    freq[tup[0]] +=1
    freq[tup[1]] +=1


# Find the complete 5 subgraph 
import networkx as nx
G=nx.Graph()
G.add_nodes_from(freq.keys())
G.add_edges_from(valid_tuples)
ans = list(nx.find_cliques(G))
#print(ans[0])
max_len = max(map(lambda x: len(x), ans))
ans = list(filter(lambda x: len(x)==max_len, ans))
print(ans)
print(sum(ans[0]))

#
#    
#                
#        