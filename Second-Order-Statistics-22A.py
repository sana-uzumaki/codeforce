# 27/10/2026
n = int(input())
s = sorted(list(set(map(int,input().split(" ")))))
print(s[1] if len(s) > 1 else "NO")