#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 19:15:05 2018

@author: simon

Xor decryption which uses numpy to decrypt
Then maps the upper case letters in string to lower
Then calculates the frequency of decrypted letters
Then calculates the absolute error from the frequency distribution of 
average english text
prints the one with the lowest score.

This is a pretty overbuilt solution

"""
import numpy as np
import csv

encrypted = []
with open('p059_cipher.txt','r') as c_file:
    for line in c_file:
        codes = line.split(',')
        for code in codes:
            encrypted.append(int(code))

encry_string = ''.join(chr(i) for i in encrypted)

encrypted = np.asarray(encrypted)

alpha = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha_code_lower = [ord(x) for x in alpha]
alpha_code_upper = [ord(x.upper()) for x in alpha]
alpha_freq = {}

with open('p059_freq.csv', 'r') as fr_csv:
    reader = csv.reader(fr_csv)
    for row in reader:
        vals = list(map(float,row))
        for index, val in enumerate(vals):
            alpha_freq.update({alpha_code_lower[index]: val})

print(alpha_freq)

#print(encry_string)

mapUptoLow = {alpha_code_upper[x]:alpha_code_lower[x] for x in range(0, len(alpha_code_lower))}

def tolow(num):
    if num in mapUptoLow:
        return mapUptoLow[num]
    else:
        return num

np_tolow = np.vectorize(tolow)

np_chr = np.vectorize(chr)

def decrypt(narr, keyarr):
    narr = np.asarray(narr, dtype=np.int)
    keyarr = np.asarray(keyarr, dtype=np.int)
    keyarr_full = keyarr.copy()
    for x in range(0, int(np.ceil(len(narr)/len(keyarr)))): 
        keyarr_full = np.append(keyarr_full, keyarr)
    assert len(narr) < len(keyarr_full)
    keyarr_full = keyarr_full[0:len(narr)]
    assert len(narr)==len(keyarr_full)
    
    return np.bitwise_xor(narr,keyarr_full)

assert list(decrypt([3,5,6,7,8], [1,2])) == [2, 7, 7, 5, 9]

def low_decrypt(narr, keyarr):
    return np_tolow(decrypt(narr, keyarr))


def freq(narr):
    narr = np.asarray(narr)
    uni, counts = np.unique(narr, return_counts=True)
    return np.asarray((uni, counts)).T

def abserr(narr, keyarr):
    out = 0
    decrypted_conv = low_decrypt(narr, keyarr)
    de_freq = freq(decrypted_conv)
    # Filter the frequency
    for code in alpha_code_lower:
        try:
            f = de_freq[de_freq[:,0]==code][0][1]
        except IndexError:
            f = 0
        relf = f/len(narr)
        out += np.abs((relf) - (alpha_freq[code]/100))
    
    return out

min_abserr = 10**2
best_key = []

for key1 in alpha_code_lower:
    for key2 in alpha_code_lower:
        for key3 in alpha_code_lower:
            err = abserr(encrypted, [key1, key2, key3])
            if err < min_abserr:
                min_abserr = err
                best_key = [key1, key2, key3]
                
        
print(best_key)
print([chr(x) for x in best_key])

out_str = decrypt(encrypted, best_key)
decrypted_str = ''.join(chr(i) for i in out_str)
print(decrypted_str)

ans = np.sum(out_str)
print(ans )
    
    

# TODO get the R2 value for the match between the letter 
# distribution and return the key which has the least result
# maybe the top 5


    
