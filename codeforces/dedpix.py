from sys import stdin,stdout

t = int(stdin.readline().strip())
for _ in range(t):
    a,b,x,y = map(int, stdin.readline().split())
    ans = max(max(x,a-x-1)*b, max(y,b-y-1)*a)
    stdout.write("{}\n".format(ans))
