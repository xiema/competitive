from sys import stdin, stdout

t = int(stdin.readline().strip())

for _ in range(t):
    h, m = map(int, stdin.readline().split())
    stdout.write("{}\n".format(60-m + (23-h)*60))
