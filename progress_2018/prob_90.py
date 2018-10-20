#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:29:37 2018

@author: simon
"""

from itertools import combinations

select = list(range(0,10))

valid_dice = []

for comb in combinations(select, 6):
    edit = set(comb)
    for tup in [(6,9), (9,6)]:
        if (tup[0] in comb) and (tup[1] not in comb):
            edit = set(list(comb) + [tup[1]])
            break
    valid_dice.append(edit)


numtups = []
for x in range(1,10):
    basestr = str(x**2)
    if len(basestr)==1:
        basestr = '0'+basestr
    numtups += [tuple(int(j) for j in basestr)]
#print(numtups)

count = 0

for d1 in valid_dice:
    for d2 in valid_dice:
        valid = True
        for numtup in numtups:
            tf1 = (numtup[0] in d1) and (numtup[1] in d2)
            tf2 = (numtup[0] in d2) and (numtup[1] in d1)
            if tf1+tf2 == 0:
                valid = False
                break
        if valid:
            count += 1
        else:
            continue

# divide by 2 to account for the double count in the dice
count = count//2
print(count)

def checkNum(d1, d2,numtup):
    pass