from sys import stdin,stdout

t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    a = [(int(b),i) for i,b in enumerate(stdin.readline().split())]
    a.sort()
    ans,c = 0,1
    for i in range(1,n):
        if a[i][1] > a[i-1][1]:
            c+=1
        else:
            ans = max(ans,c)
            c=1
    else:
        ans = max(ans,c)

    stdout.write('{}\n'.format(n-ans))
