n = int(input())
arr = list(map(int, input().split(" ")))
from collections import Counter
freq = Counter(arr)
print(min(freq[1] + freq[2], freq[1] + freq[3], freq[2] + freq[3]))