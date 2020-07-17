from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n,x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    a.sort(reverse=True)
    c,ans = 0,0
    for i in range(n):
        if a[i] >= x:
            ans+=1
        else:
            c+=1
            if a[i] * c >= x:
                ans+=1
                c=0
    stdout.write('{}\n'.format(ans))
