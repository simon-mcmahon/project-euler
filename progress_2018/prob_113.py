#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 11:25:30 2018

@author: simon
"""

def isAsc(numstr):
    if len(numstr)==1:
        return True
    for indx, char in enumerate(numstr[:-1]):
        if int(numstr[indx+1]) < int(char):
            return False
    return True

def isDec(numstr):
    if len(numstr)==1:
        return True
    for indx, char in enumerate(numstr[:-1]):
        if int(numstr[indx+1]) > int(char):
            return False
    return True

def isSame(numstr):
    firstChar = numstr[0]
    for char in numstr[1:]:
        if char != firstChar:
            return False
    return True

for x in range(1,10):
    assert isAsc(str(x))==True
    assert isDec(str(x))==True

# Unit Tests

assert isAsc('1233')==True
assert isAsc('121')==False
assert isAsc('123341') == False
assert isAsc('455589999999999999')==True
assert isAsc('4554589999999999999')==False
assert isAsc('455489999999999998')==False

assert isDec('1233')==False
assert isDec('121')==False
assert isDec('123341') == False
assert isDec('455589999999999999')==False
assert isDec('4554589999999999999')== False
assert isDec('455489999999999998')==False
assert isDec('97666')==True

assert isSame('111')==True
assert isSame('1')==True
assert isSame('55')==True
assert isSame('99999999999999999')==True
assert isSame('112')==False

# Memoize dictionary
memo = {1: (0,1,1,1,1,1,1,1,1,1)}

# procedural generation approach to generate of ascending numbers
# vectors of matching numbers ending in 0-9.
# formatted as dynamic programming so we can request what we want

def A(k2):
    # vector of 10 elements.
    try:
        return memo[k2]
    except KeyError:
        k1 = k2 - 1
        if k1 > 1:
            prev = A(k1)
            if k1 not in memo:
                memo.update({k1:prev})
        elif k1==1:
            memo.update({2:(0,1,2,3,4,5,6,7,8,9)})
            return (0,1,2,3,4,5,6,7,8,9)
        else:
            raise ValueError
        
        # Find the current values of N from previous
        curr = [0]*10 # N0k, N1k , ... , N9k
        for x in range(0,10):
            curr[x] = sum(prev[0:x+1])
        
        if k2 not in memo:
            memo.update({k2:tuple(curr)})
#            memo.update({k2:prev})

        return tuple(curr)

def Atot(n):
    return sum([sum(A(x)) for x in range(1, n+1)])

# memoization for the Descending numbers
memoD = {1: (0,1,1,1,1,1,1,1,1,1)}

# procedural generation approach to generate of ascending numbers
# vectors of matching numbers ending in 0-9.
# formatted as dynamic programming so we can request what we want

def D(k2):
    # vector of 10 elements.
    try:
        return memoD[k2]
    except KeyError:
        k1 = k2 - 1
        if k1 > 1:
            prev = D(k1)
            if k1 not in memoD:
                memoD.update({k1:prev})
        elif k1==1:

            memoD.update({2:(9,9,8,7,6,5,4,3,2,1)})
            return (9,9,8,7,6,5,4,3,2,1)
        else:
            raise ValueError
        
        # Find the current values of N from previous
        curr = [0]*10 # N0k, N1k , ... , N9k
        for x in range(0,10): # TODO conflict with the prev variable
            curr[x] = sum(prev[x:])
        
        if k2 not in memoD:
            memoD.update({k2:tuple(curr)})

        return tuple(curr)

def Dtot(n):
    return sum([sum(D(x)) for x in range(1, n+1)])

def SameTot(n):
    return 9*n

def nonBouncy(n):
    # nonBouncy are ascending + descending - duplicated Sames
    return Atot(n) + Dtot(n) - SameTot(n)

ascs = [] # counts of numbers less than 10**n

#lowpow10 = 5
powers = [1,2,3,4]
for lowpow10 in powers:
    cntAsc = 0
    cntDec = 0
    cntSame = 0
    for x in range(1,10**lowpow10):
        if isAsc(str(x)):
            cntAsc += 1
        if isDec(str(x)):
            cntDec += 1
        if isSame(str(x)):
            cntSame += 1
    # Test the ascending function working properly
    assert Atot(lowpow10) == cntAsc
    assert Dtot(lowpow10) == cntDec
#    print('asc: {}, dec: {}, same: {} less than 10**{}'.format(cntAsc, cntDec, cntSame, lowpow10))

#print('-------------------')
#
#for j in powers:
#    print('{}  asc {} dec less than 10**{}'.format(Atot(j), Dtot(j),j))

print('-------------------')

assert nonBouncy(6) == 12951
assert nonBouncy(10) == 277032

ANSWER = nonBouncy(100)
print(ANSWER)