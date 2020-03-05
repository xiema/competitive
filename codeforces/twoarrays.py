n,m = map(int, input().split())

mod = int(1e9+7)

def c(n, r):
    ret = 1
    i,j = n,1
    r = min(r, n-r)
    while j <= r:
        print(i, j, ret)
        ret *= i
        ret /= j
        i-=1
        j+=1
    return int(ret)%mod

memo = {}
def p(n, k):
    if n==0 or k==0 or k==n:
        return 1
    if (n,k) not in memo:
        memo[(n,k)] = (p(n-1,k-1) + p(n-1,k)) % mod
    return memo[(n,k)]

#print(c(n+(m*2)-1,n-1))
print(p(n+(m*2)-1,n-1))
