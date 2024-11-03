def partitions(n):
    return (lambda p: [[p.__setitem__(j, p[j] + p[j - i]) for j in range(i, n + 1)] for i in range(1, n + 1)] and p)([1] + [0] * n)[n]

print(partitions(100) - 1) 