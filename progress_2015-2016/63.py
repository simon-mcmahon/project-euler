#firstly the number to the power must be less than 10. a^n<10^n
#by exploiting the value of the log, n<=(1/(1-log(a,10))
import math as m 
count=0
for a in range(1,10):
   for n in range(0,int(m.floor((1/(1-m.log(a,10)))))+1):
       if len(str(a**n))==n:
           count+=1
print count

