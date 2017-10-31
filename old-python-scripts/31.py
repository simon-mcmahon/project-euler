

#tree approach
#recursive attempt
#decending currency amounts to gurantee uniqueness of path

den=[1,2,5,10,20,50,100,200]
n=0
def branch(amt,max_den):
    global n 
    if max_den==1 or amt==0:
        n=n+1
        return 0
    for x in range(0,den.index(max_den)+1):
        if den[x]<=amt:
            branch(amt-den[x],den[x])

branch(200,200)    
print n

