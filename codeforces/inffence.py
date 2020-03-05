from math import ceil,gcd
t = int(input().strip())
for _ in range(t):
    r,b,k = map(int, input().split())
    if r > b:
        r,b = b,r
    if ceil((b-gcd(r,b))/r) < k:
        print("OBEY")
    else:
        print("REBEL")
