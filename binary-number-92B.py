s = input()
n = len(s)
res = carry = 0
for i in range(n - 1, 0, -1):
    curV = 1 + carry if s[i] == "1" else carry
    if curV == 1:
        res += 2
        carry = 1
    else:
        res += 1
print(res + 1 if carry else res)