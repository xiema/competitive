from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n, k = map(int, stdin.readline().split())
    stdout.write("{}\n".format(n + min(0,k//2-n%k)))
