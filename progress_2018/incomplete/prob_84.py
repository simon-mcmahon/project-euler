#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 23:42:08 2018

@author: simon
"""

import csv
from fractions import Fraction, gcd
from collections import defaultdict
# Get the probability dist of 2 six sided dice

sixD_freq = defaultdict(int) 
six6_prob = {}
for d1 in range(1,7):
    for d2 in range(1,7):
        sixD_freq[d1+d2] += 1

for tot in sixD_freq:
    six6_prob.update({tot: Fraction(sixD_freq[tot], 6**2)})

# Check probability sum
assert sum(six6_prob.values()) == 1

spaces = []

with open('p084_monopolyNums.csv', 'r') as mono_file:
    reader = csv.DictReader(mono_file, fieldnames=['num','code'])
    for row in reader:
        print(row['num'], row['code'])
        spaces.append(row['code'])
        
print(spaces)