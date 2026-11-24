n = int(input())
while n > 0:
    n -= 1
    l = sorted(map(int, input().split(" ")))
    if (l[0] + 2) == l[2] and l[2] == (l[1] + 1):
        print("YES")
    else:
        print("NO")