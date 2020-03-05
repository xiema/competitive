n,a,b,k = map(int,input().split())
hlist = list(map(int,input().split()))
cnt = {}
c = a+b
for h in hlist:
    h = h%c or c
    d = 0
    if h > a:
        d = h//a - (h%a==0)
    cnt[d] = cnt.get(d,0) + 1
    
ans = 0
for d,v in sorted(cnt.items()):
    if d*v <= k:
        k -= d*v
        ans += v
    else:
        ans += k//d
        break

print(ans)
