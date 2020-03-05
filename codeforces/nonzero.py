t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    alist = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for a in alist:
        if a == 0:
            sum+=1
            cnt+=1
        else:
            sum+=a
    if sum==0:
        cnt+=1
    print(cnt)
