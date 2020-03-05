from math import sqrt,gcd

x = int(input().strip())
p = int(sqrt(x))+1
while p > 1:
    if x%p == 0 and gcd(p,x//p) == 1:
        break
    p-=1
print(p,x//p)
