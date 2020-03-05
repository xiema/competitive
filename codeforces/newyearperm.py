from sys import stdin,stdout



n,m = map(int, stdin.readline().split())

memo = {0:1}
def fac(x):
    if x not in memo:
        r = 1
        for i in range(x):
            if i in memo:
                r = memo[i]
                continue
            else:
                r = (r*i)%m
                memo[i] = r
        memo[x] = (x * r) %m
    return memo[x]

total = 0
mid = n//2+1
for i in range(1, mid):
    total = (total + fac(n-i+1)*fac(i)) % m
total = (total*(n+1)) %m
if n%2:
    total = (total + mid*fac(n-mid+1)*fac(mid)) % m

print(total)
