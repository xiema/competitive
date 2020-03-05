T = int(input())

def c (n, r):
    ret = 1
    x,y = n,1
    while y <= r:
        ret *= x
        ret /= y
        x-=1
        y+=1
    return int(ret)
out = []
for _ in range(T):
    n,k = map(int, input().split())
    out.append(str(c(n-1,k-1)))

print('\n'.join(out))
