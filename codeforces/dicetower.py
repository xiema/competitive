from sys import stdin,stdout

t = int(stdin.readline().strip())
xlist = list(map(int,stdin.readline().split()))

for x in xlist:
    k = 14+x%14
    if x >= 15 and k >= 15 and k <= 20:
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
