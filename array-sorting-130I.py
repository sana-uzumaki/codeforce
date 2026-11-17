n = int(input())
freq = {}
for i in range(n):
    j = input()
    freq[j] = freq.get(j,0) + 1
key = sorted(freq)
for i in key:
    for j in range(freq[i]):
        print(i, end=" ")
print()

# this problem need to been solved in another language