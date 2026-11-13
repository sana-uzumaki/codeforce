n = int(input())
while n > 0:
    n -= 1
    size = int(input())
    arr = list(map(int,input().split(" ")))
    maxx = float("-inf")
    point = 0
    for i in arr:
        if i >= maxx:
            maxx = i
            point += 1
    print(point)