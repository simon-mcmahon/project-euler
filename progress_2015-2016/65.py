from fractions import gcd

##frac=(num,den)

def inverse(frac):
    num=frac[0]
    den=frac[1]
    return den,num

def simpl(frac):
    num=frac[0]
    den=frac[1]
    
    return (num/gcd(num,den)),(den/gcd(num,den))

def add(frac1,frac2):
    num1=frac1[0]
    den1=frac1[1]
    num2=frac2[0]
    den2=frac2[1]
    x=(den1/gcd(den1,den2))
    y=(den2/gcd(den1,den2))
    aden=x*y*gcd(den1,den2)
    anum=num1*y+num2*x
    return anum,aden

#generate list of the continued fraction
cont_frac=[2]

for a in range(1,100):
    cont_frac+=[1,2*a,1]

#add, simpl,inverse

print add((cont_frac[0],1),(1,cont_frac[1]))

n=99 #n=3 gives 4th term

f=simpl(add((cont_frac[n-1],1),(1,cont_frac[n])))

for a in range(n-2,-1,-1):
    f=simpl(add((cont_frac[a],1),inverse(f)))

print f

def sum_dig(num):
    s=0
    for x in range(0,len(str(num))):
        s+=int(str(num)[x])
    return s

print sum_dig(f[0])

##f=inverse(simpl(add((cont_frac[1],1),(1,cont_frac[2]))))
##
##print add((cont_frac[0],1),f)
