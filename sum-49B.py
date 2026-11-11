a, b = input().split(" ")
res = 0
base = max(int(i) for i in a + b)
for i in range(base + 1, 21):
    ax = int(a, i)
    bx = int(b, i)
    cur = ax + bx
    n = 0
    while cur > 0:
        n += 1
        cur //= i
    res = max(res,n)
print(res)