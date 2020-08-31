from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    a,b = map(int, stdin.readline().split())
    d = min(abs(a-b),a,b)
    c = d + (2*(min(a,b)-d))//3
    stdout.write('{}\n'.format(c))
