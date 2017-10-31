s=range(1,1000)
s=filter(lambda x: (x%5==0) or (x%3==0),s)
print sum(s)
