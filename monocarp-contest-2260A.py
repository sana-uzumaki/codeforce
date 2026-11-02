n = int(input())
while n > 0:
    n -= 1
    size = int(input())
    lis = list(map(int,input().split(" ")))
    if lis[0] == 0 and lis[-1] == 0:
        print(0)
    else:
        from collections import Counter
        freq = Counter(lis)
        if freq[0] >= 2:
            point = (lis[0] == 1) + (lis[-1] == 1)
            print(point)
        else:
            print(-1)