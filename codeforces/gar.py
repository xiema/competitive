n = int(input().strip())
even,odd = n//2,n//2+n%2

ints = list(map(int, input().split()))
prev,previ,count = None,-1,0
complexity = 0
groups = []
for i,x in enumerate(ints):
    if x==0:
        count+=1
    else:
        if not prev:
            if count:
                groups.append((1,-count,x%2))
        elif prev%2 == x%2:
            if count:
                groups.append((2,-count,x%2))
        else:
            complexity+=1
        if x%2:
            odd-=1
        else:
            even-=1
        count = 0
        prev=x
else:
    if count:
        if prev:
            groups.append((1,-count,prev%2))
        else:
            if n%2==0:
                complexity = 1

if groups:
    groups.sort(reverse=True)
    for g in groups:
        if g[2]:
            if odd + g[1] < 0:
                complexity+=g[0]
            else:
                odd+=g[1]
        else:
            if even + g[1] < 0:
                complexity+=g[0]
            else:
                even+=g[1]
print(complexity)
