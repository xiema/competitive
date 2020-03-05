from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    a,b = map(int, stdin.readline().split())
    c = 0
    b+=1
    while b >= 10:
        b//=10
        c+=1
    stdout.write("{}\n".format(c*a))
