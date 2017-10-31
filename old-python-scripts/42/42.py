words_file = open('p042_words.txt', 'r')
words=words_file.readlines()
oneword=words[0].split(',')
for x in range(0,len(oneword)):
    oneword[x]=oneword[x].replace('"','')

alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#A=0 etc. so add 1 to get alpha value

wordsum=[]

for a in range(0,len(oneword)):
    count=0
    for x in range(0,len(oneword[a])):
        count+=alpha.index(oneword[a][x])+1
    wordsum+=[count]

#generate triangle numbers

triangle=[]
for x in range(1,50):
    triangle+=[sum(range(1,x+1))]

print len(filter(lambda x: x in triangle, wordsum))
#length of the array of wordsums equal to a triangle number



