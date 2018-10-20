def reverse(i):
    s = str(i)
    return int(s[::-1])

memo = {}

def lych(i, cnt):
    # print(cnt)
    if i in memo:
        return memo[i]
    if cnt >= 50:
        memo.update({i:1})
        return 1
    new_num = i + reverse(i)
    if str(new_num)[::-1] == str(new_num): #Palemdrome condition
        memo.update({i:0})
        return 0
    else:
        return lych(new_num, cnt + 1)

nums = list(range(1,10**4))

ans = sum(map(lambda x: lych(x,1), nums))

print(ans)
