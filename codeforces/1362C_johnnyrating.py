from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    a,c = 2,0
    while n:
        if n%2:
            c += a-1
        a *= 2
        n //= 2
    stdout.write('{}\n'.format(c))
