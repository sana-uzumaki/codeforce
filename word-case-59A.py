s = input()
upper = lower = 0
for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print(s.upper() if (upper - lower) > 0 else s.lower())