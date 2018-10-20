#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 18:08:41 2018

@author: simon
"""

import csv

minsOnes = {0:'', 1:'I', 2:'II', 3: 'III', 4:'IV', 5:'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
minsTens = {0:'', 1:'X', 2:'XX', 3: 'XXX', 4:'XL', 5:'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
minsHundreds = {0:'', 1:'C', 2:'CC', 3: 'CCC', 4:'CD', 5:'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
letter_ord = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
rom_val = {'M':1000, 'D':500, 'C': 100, 'L':50, 'X': 10, 'V':5, 'I': 1}

def rom_add(str1):
    total = 0
    str1 = str1.strip()
    for x in range(0, len(str1)):
        if x <= len(str1) - 2: #Not the end character
            if letter_ord.index(str1[x+1]) > letter_ord.index(str1[x]):
                total -= rom_val[str1[x]]
            else:
                total += rom_val[str1[x]]
        else:
            total += rom_val[str1[x]]
    return total

def rom_str(number):
    rom_str = ''
    ones_str = ''
    tens_str = ''
    hun_str = ''
    thou_str = ''
    
    try:
        ones_str = minsOnes[int(str(number)[-1])]
        tens_str = minsTens[int(str(number)[-2])]
        hun_str = minsHundreds[int(str(number)[-3])]
        thou_str = 'M' * int(str(number)[0:-3])
    except (IndexError, ValueError):
        pass
   
    rom_str = thou_str + hun_str + tens_str + ones_str

    return rom_str

ans = 0 

max_tot = 0
rom_val = {'M':1000, 'D':500, 'C': 100, 'L':50, 'X': 10, 'V':5, 'I': 1}
letter_ord = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
numbers = []
with open('p089_roman.txt', 'r') as f:
    for line in f:
        total = rom_add(line)
        diff =  len(line.strip()) - len(rom_str(total))
        ans += diff

print(ans)

# CHECK THE ROMAN STRING FUNCTION (first 1000)

with open('p089_roman_check.csv', 'r') as check_csv:
    reader = csv.DictReader(check_csv)
    for row in reader:
        try:
            assert rom_str(row['number'])== row['roman_numeral']

        except AssertionError:
            print('number {} not equal. {} != {}'.format(row['number'], rom_str(row['number']), row['roman_numeral']))
        
    
