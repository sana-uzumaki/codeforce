n = int(input())
while n > 0:
    n -= 1
    size = int(input())
    l = list(map(int, input().split(" ")))
    s = {l[0]}
    res = l[0]
    for i in range(1, size):
        ns = set()
        for j in s:
            plus = l[i] + j
            minus = l[i] - j
            res = max(res, plus, minus, l[i])
            ns.add(plus + j)
            ns.add(minus + j)
            ns.add(l[i] + j)  
        s = ns
    print(res)