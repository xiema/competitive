t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    alist = list(map(int,input().split()))
    c = 0
    for a in alist:
        if a%2:
            c+=1
    if c and (c%2 or c!=n):
        print("YES")
    else:
        print("NO")
