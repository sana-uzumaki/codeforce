a, b = list(map(int,input().split()))
maxx = max(a, b)
need = (6 - maxx) + 1
from math import gcd
div = gcd(need, 6)
print(f"{need // div}/{6 // div}")