from collections import Counter
n = int(input())
while n > 0:
    n -= 1
    size, k = map(int, input().split(" "))
    l = list(map(int, input().split(" ")))
    freq = Counter(l)
    rem = 0
    for i in range(size + 2):
        if i not in freq:
            print(i)
            break
        if freq[i] >= k:
            rem += (freq[i] - k)
        elif (rem + freq[i]) >= k:
            rem -= (k - freq[i])
        else:
            print(i)
            break