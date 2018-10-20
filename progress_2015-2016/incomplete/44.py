###first n pent numbers
##n=10**4
##pent=range(1,n+1)
##pent=map(lambda x: x*(3*x-1)/2,pent)

#wlog p_j > p_k

#brute force method
##pairs=[]
##
##for j in range(0,len(pent)):
##    for k in range(0,j+1):
##        if (pent[j]+pent[k] in pent) and ((pent[j]-pent[k])in pent):
##            pairs+=[pent[k],pent[j]]


#make lists of odd and even ones

##odd=filter(lambda x: (x%2!=0),pent)
##even=filter(lambda x: (x%2==0),pent)
##
#p_n must be same odd/even as p_m

#3j**2-j-3k**2+k=

##n=10**3
##twopent=range(1,n+1)
##twopent=map(lambda x: x*(3*x-1),twopent)
##
##import itertools as it
##
##def check(tup):
##    j=tup[1]
##    k=tup[0]
##    A=3*j**2-k+3*k**2+k
##    if A in twopent:
##        return 1
##    else:
##        return 0
##pairs=[]
##
##for j in range(1,10**5):
##    min_dif=3*j+1
##    for k in range(int((min_dif-1)/3)-1,j):
##        if check((j,k))==1:
##            pairs+=(j,k)


alpha=range(1,10**5)
# keep only alpha is 1 mod 6
alpha=filter(lambda x: (x%6==5) and (x%2!=0) and (x%3!=0),alpha)
A=map(lambda x: int((x**2-1)/12),alpha)
n=map(lambda x: (1+x)/6,alpha)

def check(k):
    return map(lambda x: x+3*k**2-k,A)



