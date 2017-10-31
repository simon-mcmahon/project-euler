names_file = open('p022_names.txt', 'r')
names=names_file.readlines()
names=names[0].split(',')
for x in range(0,len(names)):
    names[x]=names[x].replace('"','')

names.sort()

alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#A=0 etc. so add 1 to get alpha value

wordsum=[]

for a in range(0,len(names)):
    count=0
    for x in range(0,len(names[a])):
        count+=alpha.index(names[a][x])+1
    wordsum+=[(a+1)*count]

print sum(wordsum)  
