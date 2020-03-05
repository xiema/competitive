from sys import stdin,stdout
t = int(stdin.readline().strip())
for _ in range(t):
    n,m = map(int,stdin.readline().split())
    ans = None
    if m == 0:
        ans = 0
    elif m*2 >= n:
        ans = (n*(n+1)//2) - (n-m)
    else:
        q = (n-m)//(m+1)
        r = (n-m)%(m+1)
        ans = (n*(n+1)//2) - ((m+1)*q + 2*r)*(q+1)//2
    stdout.write("{}\n".format(ans))
