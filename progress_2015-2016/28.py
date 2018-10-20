#each inside nest square are the odd integers 1,3,5 etc.
#corners are the formed in 4's from the previous highest corner added to the (square length-1)
# e.g. 1+2*1,1+2*2,1+2*3,1+2*4,9+4*1,...

diag=[1]
for a in range(1,500+1): #from 1-1001 or 1-500
    last=diag[-1]

    diag+=[last+1*2*a,last+2*2*a,last+3*2*a,last+4*2*a]

print sum(diag)
