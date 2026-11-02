n = int(input())
while n > 0:
    n -= 1
    size = int(input())
    array = list(map(int,input().split(" ")))
    rumble = []
    for ind, val in enumerate(array):
        if (ind + 1) != val:
            rumble.append(val)
    i = 0
    m = len(rumble) - 1
    while i < m:
        i += 1
    checkRumble = sorted(rumble,reverse=True)
    if checkRumble == rumble:
        print("YES")
    else:
        print("No")