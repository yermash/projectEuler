from helpers import *

n = ''.join(str(i) for i in range(1, 185186))
final = [int(n[10**i - 1]) for i in range(7)]

print(listProd(final))