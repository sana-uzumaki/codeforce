n = int(input())
arr = list(map(int,input().split(" ")))
s = sum(arr)
res = []
for ind, val in enumerate(arr):
    if (s - val) == (val * (n - 1)):
        res.append(ind + 1)
print(len(res))
print(*res)