from collections import Counter
priceN, fruitN = list(map(int,input().split(" ")))
price = list(map(int,input().split(" ")))
price.sort()
fruits = []
for i in range(fruitN):
    fruits.append(input())
count = Counter(fruits)
key = sorted(count, key=lambda x: count[x])
minVal = maxVal = 0
uid = len(key)
for i in key:
    maxVal += price[priceN - uid] * count[i]
    uid -= 1
uid = len(key) - 1
for i in key:
    minVal += price[uid] * count[i]
    uid -= 1
print(minVal, maxVal)