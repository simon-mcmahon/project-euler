#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:33:08 2018

@author: simon
"""

#(n/d) > (3/7)
#(7n) > (3d)
#n >= ceil((3d)/7)
#
#(n/d) + ep = (3/7)
#ep = (3/7) - (n/d) = (3*d-7*n)/(7d)

import numpy as np

f = (3/7)
r = np.arange(1,10**6+1)
candidates = np.ceil(r*(3/7)) - 1
diff = (np.divide(candidates,r) - f)
narr = np.where(diff < 0 , diff, 1)
n = np.argmax(narr) # index of the best match
print(int(candidates[n]))
print('fraction answer to left of 3/7 is {}/{}'.format(int(candidates[n]), r[n]))

# fraction answer to left of 3/7 is 428570/999997