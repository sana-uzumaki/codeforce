def find_prime(div):
    prime = [0 for _ in range(div + 1)]
    for i in range(2,div + 1):
        if prime[i] >= 1:
            continue
        for j in range(i + i, div + 1, i):
            prime[j] += 1
    return [i for i in range(2,div + 1) if prime[i] == 0]
start, end, div = list(map(int,input().split(" ")))
primes = find_prime(div)
if not primes or primes[-1] != div:
    print(0)
else:
    primes.pop()
    res = 0
    for i in range(start, end + 1):
        if div == 2:
            if i % 2 == 0:
                res += 1
            continue
        elif div == 3:
            if i % 2 == 1 and i % 3 == 0:
                res += 1
            continue
        flag = True
        for j in primes:
            if i % j == 0:
                flag = False
                break
        if flag and i % div == 0:
            res += 1
    print(res)

# need to optmize this code