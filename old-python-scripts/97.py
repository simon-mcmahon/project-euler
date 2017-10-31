

def keep_10(num):
    if len(str(num))<=10:
        return num
    else:
        return int(str(num)[len(str(num))-10:len(str(num))])

a=1
for x in range(0,7830457):
   a=2*a
   a=keep_10(a)

print keep_10(28433*a+1)
