from sys import stdin,stdout
t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    alist = list(map(int,stdin.readline().split()))
    alist.sort()
    stdout.write("{}\n".format(alist[n]-alist[n-1]))
