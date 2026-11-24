a = list(map(int, input().split()))
ops = input().split()
ans = float('inf')
for i in range(4):
    for j in range(i + 1, 4):
        x = a[i] + a[j] if ops[0] == '+' else a[i] * a[j]
        b = [a[k] for k in range(4) if k != i and k != j]
        b.append(x)
        for p in range(3):
            for q in range(p + 1, 3):
                y = b[p] + b[q] if ops[1] == '+' else b[p] * b[q]
                z = b[3 - p - q]
                result = y + z if ops[2] == '+' else y * z
                ans = min(ans, result)
print(ans)