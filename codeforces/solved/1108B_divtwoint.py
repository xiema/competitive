from sys import stdin

n = int(stdin.readline().strip())
d = list(map(int, stdin.readline().split()))
d.sort(reverse=True)

if d[0] == d[1]:
    x,y = d[0],d[0]
else:
    x = d[0]
    i = 1
    while x%d[i]==0 and d[i+1]!=d[i]:
        i+=1
    y = d[i]

print(x,y)
