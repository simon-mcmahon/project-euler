fibb=[1,1]
while fibb[-1]<4*10**6:
    fibb+=[fibb[-1]+fibb[-2]]
fibb=filter(lambda x: (x%2==0),fibb)
print sum(fibb)
