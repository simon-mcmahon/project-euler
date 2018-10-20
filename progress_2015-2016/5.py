n=20
p=range(2,n+1)
for a in [2]+range(3,n+1,2):
    p=filter(lambda x: (x%a!=0) or (x==a),p)

import math as m

num=1

for x in range(0,len(p)):
    num=num*p[x]**(m.floor(m.log(20,p[x])))

print num
