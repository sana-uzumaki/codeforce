n, m = list(map(int,input().split(" ")))
s = ""
f = True
for i in range(n):
    curS = input()
    se = set()
    for j in curS:
        se.add(j)
    if len(se) != 1 or s == curS:
        f = False
        break
    s = curS
print("YES" if f else "NO")