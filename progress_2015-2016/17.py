ones=['one','two','three','four','five','six','seven','eight','nine']
tens=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
others=['hundred','thousand']

def spell(num):
    s=str(num)
    output=''
    for a in range(0,len(s)):
        if int(s[a])!=0 and (len(s)-a)>=3:
            output+=ones[int(s[a])-1] +' ' +  others[(len(s)-a)-3] + ' '
        elif int(s[a])!=0 and int(s[a])!=1 and(len(s)-a)==2:

            if len(s)>2:
                output+='and ' + tens[int(s[a])-1] + ' ' #exclude and when two digits
            if len(s)==2:
                output=tens[int(s[a])-1] + ' '


        elif int(s[a])==1 and (len(s)-a)==2: #accounting for 15 case

            if len(s)>2:
                output+='and ' + teens[int(s[a+1])]
            if len(s)==2:
                output=teens[int(s[a+1])]
            break
        elif int(s[a])==0 and(len(s)-a)==2: #accounting for the and condition
            if int(s[a+1])!=0:
                output+='and'
            elif int(s[a+1])==0:
                output+=''
        elif int(s[a])!=0 and(len(s)-a)==1:
            output+=ones[int(s[a])-1] + ' '
    return output
print spell(1502).replace(' ','')

answer=''
for x in range(1,1001):
##    print spell(x)
    answer+=spell(x).replace(' ','')

print len(answer)
