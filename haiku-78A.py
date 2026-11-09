first = input()
second = input()
thrid = input()
from collections import Counter
count1 = Counter(first)
count2 = Counter(second)
count3 = Counter(thrid)
vowel = "aeiou"
c1 = c2 = c3 = 0
for i in vowel:
    c1 += count1[i]
    c2 += count2[i]
    c3 += count3[i]
if c1 == 5 and c2 == 7 and c3 == 5:
    print("YES")
else:
    print("NO")