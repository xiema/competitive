from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    c = list(map(int, stdin.readline().split()))
    c.sort(reverse=True)
    total = c[1]-c[2]
    c[0],c[1] = c[0]-total,c[1]-total
    k = min(c[0]-c[1],c[1])
    total += k*2
    c[1] = c[1] - k
    total += 3*(c[1]//2) + c[1]%2
    stdout.write("{}\n".format(total))
