from sys import stdin,stdout
t = int(stdin.readline().strip())
for _ in range(t):
    n,d = map(int,stdin.readline().split())
    total = 0
    for i,a in enumerate(list(map(int,stdin.readline().split()))):
        c = a*i
        if c > d:
            total += d//i
            break
        total += a
        d -= c
    stdout.write("{}\n".format(total))
