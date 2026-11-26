n = int(input())
while n > 0:
    n -= 1
    step = 0
    a, b, c = sorted(list(map(int, input().split())))
    while not (a == b or b == c or a == c):
        a += 1
        c -= 1
        a, b, c = sorted([a, b, c])
        step += 1
    print(step)