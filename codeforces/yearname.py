from sys import stdin,stdout

n,m = map(int, stdin.readline().split())
s = stdin.readline().split()
t = stdin.readline().split()
q = int(stdin.readline().strip())
years = [int(stdin.readline().strip()) for _ in range(q)]
for y in years:
    stdout.write("{}{}\n".format(s[(y-1)%n],t[(y-1)%m]))
