powers = [i ** 5 for i in range(10)]

final = 0
for i in range(2, 7*9**5):
    n = i
    s = 0
    while n:
        s += powers[n % 10]
        n //= 10
    if s == i:
        final += i
print(final)
        