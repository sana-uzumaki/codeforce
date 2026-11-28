n = int(input()) - 1
l = list(map(int, input().split()))
i = a = b = 0
lsum = rsum = 0
while i <= n:
    if lsum <= rsum:
        lsum += l[i]
        i += 1
        a += 1
    else:
        rsum += l[n]
        n -= 1
        b += 1
print(a, b)