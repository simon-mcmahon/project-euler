#the possible paths is the sun of the previous 2 lattices in a square with the top
#most and down most paths all as 1's. It is pascals triangle and the amount of
#possible paths for an n X n square is the central number of the triangle
# and it is the 2n row. Hence, the answer is (2n) C (n)

import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

print ncr(20*2,20)
