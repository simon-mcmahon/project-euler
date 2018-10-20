from collections import defaultdict
x = 1

def freq_dict(lst):
    digs = defaultdict(int)
    lst = str(lst)
    for j in lst:
        digs[j] += 1
    return digs

while True:
    if x % 1000 == 0:
        print(x)
    if len(str(6*x))!= len(str(x)):
        x += 1
        continue
    base_digs = freq_dict(x)
    exit_bool = True
    for j in [6*x, 5*x, 4*x, 3*x, 2*x]:
        if freq_dict(j) != base_digs:
            exit_bool = False
            break
    if exit_bool:
        break
    else:
        x +=1 
        continue

print(x)
