dig=[]
for a in range(100,1000):
    for b in range(100,a+1):
        if str(a*b)[::-1]==str(a*b):
            dig+=[a*b]
print max(dig)



        
