from sys import stdin,stdout
t = int(stdin.readline().strip())
for _ in range(t):
    x,y,a,b = map(int,stdin.readline().split())
    ans = -1
    if (y-x)%(a+b)==0:
        ans = (y-x)//(a+b)
    stdout.write("{}\n".format(ans))
