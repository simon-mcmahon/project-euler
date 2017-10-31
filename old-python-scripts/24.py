import itertools as it

lexo=list(map(int,list(map("".join,it.permutations('1234567890', 10)))))
lexo.sort()
print lexo[10**6-1]
