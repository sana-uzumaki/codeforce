from collections import Counter
s1 = input()
s2 = input()
s1 = s1.replace(" ","")
count = Counter(s1)
flag = True
for i in s2:
    if i == " ":
        continue
    if i in count and count[i] > 0:
        count[i] -= 1
        continue
    flag = False
    break
print("YES" if flag else "NO")