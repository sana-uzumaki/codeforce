a = int(input())
res = 0
for i in range(2,a):
    x = a
    while x > 0:
        res += x % i
        x //= i
from math import gcd
g = gcd(res, a - 2)
print(f"{res // g}/{(a - 2) // g}")