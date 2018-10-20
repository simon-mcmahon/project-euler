
def collatz(num):
    n=num
    path=1
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        path+=1
    return path
max_num=0
max_path=1
for x in range(1,10**6):
    if collatz(x)>max_path:
        max_num=x
        max_path=collatz(x)

print str(max_num) + " and path length is " + str(max_path)
