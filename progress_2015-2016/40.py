length=0

num=1
d1=1
s=''
d10=''
d100=''
d1000=''
d10000=''
d100000=''
d1000000=''


while True:
##    s+=str(num)
    length=length+len(str(num))
##    print length
    if length>=10 and d10=='':
        d10=int(str(num)[len(str(num))-(length-10)-1])
        
    if length>=100 and d100=='':
        d100=int(str(num)[len(str(num))-(length-100)-1])
        
    if length>=1000 and d1000=='':
        d1000=int(str(num)[len(str(num))-(length-1000)-1])
        
    if length>=10000 and d10000=='':
        d10000=int(str(num)[len(str(num))-(length-10000)-1])
        
    if length>=100000 and d100000=='':
        d100000=int(str(num)[len(str(num))-(length-100000)-1])
        
    if length>=1000000 and d1000000=='':
        d1000000=int(str(num)[len(str(num))-(length-1000000)-1])
        break
    num+=1

print d1*d10*d100*d1000*d10000*d100000*d1000000
