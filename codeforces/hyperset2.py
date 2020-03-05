
from sys import stdin,stdout
n,k = map(int,stdin.readline().split())

convert = {
('S','S'):'S',('E','E'):'E',('T','T'):'T',
('S','E'):'T',('E','S'):'T',
('S','T'):'E',('T','S'):'E',
('E','T'):'S',('T','E'):'S',
}

def match(a,b):
    return ''.join(convert[(a[i],b[i])] for i in range(len(a)))


c = set()
cnx = {}
for _ in range(n):
    s = stdin.readline().strip()
    c.add(s)
    cnx[s] = set()

cnt = 0
while c:
    c1 = c.pop()
    for c2 in c:
        if c1==c2 or c2 in cnx[c1]:
            continue
        m = match(c1,c2)
        if m in c:
            cnx[c1].add(m)
            cnx[c2].add(m)
            cnt+=1

stdout.write(str(cnt))
