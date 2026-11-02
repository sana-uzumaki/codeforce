# 20/10/2026
n, m = list(map(int,input().split(" ")))
totalSquare = n * m
if totalSquare % 2 == 0:
    print(totalSquare // 2)
else:
    print((totalSquare - 1) // 2)