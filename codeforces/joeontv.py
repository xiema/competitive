from decimal import *

#n = int(input().strip())

def sum (n):
    seen = set()
    sum1 = 1
    sum2 = 1
    for i in range(2,n+1):
        if i not in seen:
            x,y = 1,i
            while True:
                _y = y*i
                if _y > n:
                    break
                x,y = x+y,_y
                seen.add(y)
            s = Decimal(x)/Decimal(y)
            sum1 += s
        sum2 += 1/i

    err = abs(sum1-Decimal(sum2))/sum1
    return err

for i in range(99990, 100000):
    e = sum(i)
    print(i, e)
