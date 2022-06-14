from sys import stdin, stdout

q,x = map(int, stdin.readline().split())

d = {i:0 for i in range(x)}
segs = {0 : 0}
queries = []
for _ in range(q):
    i = int(stdin.readline().strip())%x
    queries.append(i)
    d[i] += 1

m = min(d.values())
cur = next(filter(lambda x: x[1]==m, d.items()))[0] + m*x

lines = []
for i in reversed(queries):
    lines.append("{}\n".format(cur))
    d[i]-=1
    cur = min(d[i]*x+i,cur)

stdout.writelines(reversed(lines))
