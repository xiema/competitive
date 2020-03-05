from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    a,b,c,n = map(int, stdin.readline().split())
    d = max([a,b,c])
    n -= 3*d-a-b-c
    if n < 0 or n%3:
        stdout.write("NO\n")
    else:
        stdout.write("YES\n")
