n,m = map(int, input().split())

mod = int(1e9+7)

memo = {}
def p(n, k):
    if n==0 or k==0 or k==n:
        return 1
    if (n,k) not in memo:
        memo[(n,k)] = (p(n-1,k-1) + p(n-1,k)) % mod
    return memo[(n,k)]

print(p(n+(m*2)-1,n-1))
