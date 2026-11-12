h, t = list(map(int,input().split()))
h *= 100
t *= 10
flag = True
while t >= 20 and (h + t) >= 220:
    if flag:
        if h >= 200 and t >= 20:
            h -= 200
            t -= 20
        elif h == 100 and t >= 120:
            h = 0
            t -= 120
        elif t >= 220:
            t -= 220
    else:
        if t >= 220:
            t -= 220
        elif t >= 120 and h >= 100:
            t -= 120
            h -= 100
        elif t >= 20 and h >= 200:
            t -= 20
            h -= 200
    flag = not flag 
if flag:
    print("Hanako")
else:
    print("Ciel")