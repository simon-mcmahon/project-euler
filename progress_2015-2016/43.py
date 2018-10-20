
#generate pan_list
pan_list=[1,12,21]
for n in range(2,9):
    ndiglist=filter(lambda x: len(str(x))==n,pan_list)
    adding=[] #numbers to be added
    for x in range(0,len(ndiglist)):
        adding=[]
        for a in range(0,n+1):
            adding+=[int(str(ndiglist[x])[0:a]+str(n+1)+str(ndiglist[x])[a:len(str(ndiglist[x]))])]
        pan_list+=adding
pan_list=filter(lambda x: len(str(x))==9,pan_list)

#at this point. all 9-length pan 1-9. now convert to 10 length with 0

ndiglist=filter(lambda x: len(str(x))==9,pan_list)
adding=[] #numbers to be added
for x in range(0,len(ndiglist)):
    adding=[]
    for a in range(0,len(str(ndiglist[x]))+1):
        adding+=[int(str(ndiglist[x])[0:a]+str(0)+str(ndiglist[x])[a:len(str(ndiglist[x]))])]
    pan_list+=adding

#done. now filter the 10 digit length ones

pan_list=filter(lambda x: len(str(x))==10,pan_list)

##pan_list.sort()
##pan_list.reverse() #highest first

def sub_str(num):
    d234=int(str(num)[1:4])
    d345=int(str(num)[2:5])
    d456=int(str(num)[3:6])
    d567=int(str(num)[4:7])
    d678=int(str(num)[5:8])
    d789=int(str(num)[6:9])
    d8910=int(str(num)[7:10])
    if (d234%2==0) and (d345%3==0) and (d456%5==0) and (d567%7==0) and (d678%11==0) and (d789%13==0) and (d8910%17==0):
        return 1
    else:
        return 0

sum=0

for x in range(0,len(pan_list)):
    if sub_str(pan_list[x])==1:
        sum+=pan_list[x]

print sum 
