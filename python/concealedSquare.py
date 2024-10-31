n = 1929394959697989990
q = 1020304050607080900

def isMatch(n):
    square = n**2
    r2l = [0,9,8,7,6,5,4,3,2,1]
    j = 0
    while square > 100:
        dig = square % 10
        if dig != r2l[j]:
            return False
        j+=1
        square //= 100
    return True

for i in range(int(q**.5),int(n**.5)):
    if isMatch(i):
        print(i)