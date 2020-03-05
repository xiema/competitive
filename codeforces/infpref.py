T = int(input().strip())

for _ in range(T):
    n,x = map(int, input().split())
    s = input().strip()

    cnt = {}
    bal = 0
    lo,hi = None,None
    for c in s:
        if c == '0':
            bal+=1
        else:
            bal-=1
        cnt[bal] = cnt.get(bal,0)+1
        lo = min(lo,bal) if lo else bal
        hi = max(hi,bal) if hi else bal

    if bal == 0:
        if x >= lo and x <= hi:
            print("-1")
        else:
            print("0")
    else:
        total = 0
        if x == 0:
            total+=1
        if bal < 0 and x < lo:
            x += bal*((lo-x)//bal)
        elif bal > 0 and x > hi:
            x += bal*((hi-x)//bal)
        while x in cnt:
            total+=cnt[x]
            x-=bal
        print(total)
