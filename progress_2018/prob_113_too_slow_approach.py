#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 12:27:55 2018

@author: simon
"""

# Lets use a dynamic programming approach
# DOESNT WORK FOR 10^100 
#  A counting method is more likely appropriate.

digs = ['0','1','2','3','4','5','6','7','8','9']

def isBouncy(numstr):
    if len(numstr)<=2:
        return False
    isincr = True
    isdecr = True
    for x in range(1, len(numstr)):
#        print(x)
        isincr = (int(numstr[x]) >= int(numstr[x-1])) and isincr
        isdecr = (int(numstr[-x]) <= int(numstr[-(x+1)])) and isdecr
        if (isincr== False) and (isdecr == False):
            return True
    return False


##strings = set()
#
bouncies = [set() for x in range(3,21)]
bounciesTest = [set() for x in range(3,21)]

nonbouncies = [set() for x in range(3,21)]
#
def numBouncy(numstr,maxLength):
#    print(numstr)
    if isBouncy(numstr):
        bouncies[len(numstr)-3].add(numstr)
        return int('1'*(maxLength+1-len(numstr)))
    elif (len(numstr) >= maxLength): # not bouncy
        return 0
#    elif len(numstr)
    elif (len(numstr) < maxLength):
        return sum([numBouncy(numstr + k, maxLength) for k in digs])
    else:
        raise ValueError
lesspow1ORIG = 4
ans = sum([numBouncy(k, lesspow1ORIG) for k in digs[1:]])

#assert ans == (10**6 - 12951)

# Once a number is bouncy it stays that way.
# So iterate over the non bouncy integers and if they are bouncy add them 
# the bouncy list
# don't add the ones where 0 is the first digit 

# Get the nonbouncy 3-long numstrs
from itertools import product

lesspow10 = 4

bounciesTest[0] = bouncies[0].copy()

for perm in product(digs, repeat=3):
    numstr = ''.join(perm)
#    if numstr[0]=='0' or numstr[1]=='0':
#        continue
    if numstr not in bounciesTest[0]:
        nonbouncies[0].add(numstr)

for j in range(0, lesspow10-3):
    print(j)
    for nonbounce in nonbouncies[j]:
        for dig in digs:
            newNumstr = nonbounce + dig
    #        print(newNumstr)
            if (isBouncy(newNumstr)==True) and (newNumstr[0]!='0'):
                bounciesTest[len(newNumstr)-3].add(newNumstr)
            elif not isBouncy(newNumstr):
                nonbouncies[len(newNumstr)-3].add(newNumstr)

totals = [len(bounciesTest[x])*int('1'*(lesspow10 - 2 - x)) for x in range(0,lesspow10-2)]

print('{} bouncy and {} non-bouncy under 10**{}'.format(sum(totals), (10**lesspow10-sum(totals)-1),lesspow10))


#print(sum(totals))


#for nonbounce in nonbouncies[1]:
#    for dig in digs:
#        newNumstr = nonbounce + dig
##        print(newNumstr)
#        if (isBouncy(newNumstr)==True) and (newNumstr[0]!='0'):
#            bounciesTest[len(newNumstr)-3].add(newNumstr)
#        elif not isBouncy(newNumstr):
#            nonbouncies[len(newNumstr)-3].add(newNumstr)

#def numNonbounncy():
#    passs
#
for x in range(0,len(bouncies)):
    print('bouncies {}, bounciesTest {}'.format(len(bouncies[x]), len(bounciesTest[x])))
    print('nonbouncies {}'.format(len(nonbouncies[x])))
#
#print('{} bouncy and {} non-bouncy under 10**{}'.format(ans, (10**lesspow10-ans-1),lesspow10))
