# 19/10/2026
n, m = list(map(int,input().split(" ")))
container = []
for i in range(m):
    container.append(tuple(map(int,input().split(" "))))
container.sort(key=lambda x: -x[1])
i = 0
nn = len(container)
res = 0
while i < nn and n > 0:
    can = min(n,container[i][0])
    n -= can
    res += can * container[i][1]
    i += 1
print(res)