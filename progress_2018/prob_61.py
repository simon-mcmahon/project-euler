#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:11:30 2018

@author: simon
"""
import networkx as nx
from collections import defaultdict
n = 1

G = nx.DiGraph()
freq = defaultdict(int)

while True:
    # Note integer division done to avoid floats (they're all integers anyway)
    gon_nums = [n*(n+1)//2, n**2, n*(3*n-1)//2, n*(2*n-1), n*(5*n-3)//2, n*(3*n-2)]
    print(gon_nums)
    for num in gon_nums:
        if (num>=10**3) and (num<10**4):
            edge = (str(num)[0:2], str(num)[2:])
            print(edge)
            G.add_edge(*edge)
            freq[num] += 1
    if len([num for num in gon_nums if num>=10**4])==len(gon_nums):
        break
            
    n += 1
    
#    if n >=4:
#        break

print(freq)
print(list(nx.dag_longest_path(G)))
#freq