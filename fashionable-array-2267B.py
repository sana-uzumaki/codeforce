from collections import Counter
n = int(input())
while n > 0:
    n -= 1
    size = int(input())
    l = list(map(int,input().split(" ")))
    c = Counter(l)
    key = sorted(c,reverse=True)
    res = []
    while key:
        curKey = []
        for i in key:
            res.append(i)
            c[i] -= 1
            if c[i] != 0:
                curKey.append(i)
        key = curKey
    for i in res:
        print(i,end=" ")
    print()
