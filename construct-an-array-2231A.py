# 31/10/2026
n = int(input())
while n > 0:
    n -= 1
    size = int(input())
    num = size * 2
    res = []
    while len(res) < size:
        res.append(num)
        num -= 1
    print(*res)