start, end, div = list(map(int,input().split(" ")))
res = 0
for i in range(start, end + 1):
    if div == 2:
        if i % 2 == 0:
            res += 1
        continue
    elif div == 3:
        if i % 2 == 1 and i % 3 == 0:
            res += 1
        continue
    flag = True
    for j in range(2,div):
        if i % j == 0:
            flag = False
            break
    if flag and i % div == 0:
        res += 1
print(res)