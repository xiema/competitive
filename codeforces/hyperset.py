from sys import stdin,stdout
n,k = map(int,stdin.readline().split())
cards = set()
for _ in range(n):
    cards.add(stdin.readline().strip())
convert = {
    ('S','E'):'T',('E','S'):'T',
    ('S','T'):'E',('T','S'):'E',
    ('E','T'):'S',('T','E'):'S',
}

def match(a,b):
    ret = []
    for i in range(k):
        if a[i] == b[i]:
            ret.append(a[i])
        else:
            ret.append(convert[(a[i],b[i])])
    return ''.join(ret)

cnt = 0
while cards:
    scan = set()
    scan.add(cards.pop())
    b = True
    while b:
        b = False
        for x in cards:
            new = set()
            for y in scan:
                z = match(x,y)
                if z in cards and z not in new:
                    new.add(x)
                    new.add(z)
                    cnt+=1
            scan.update(new)
        cards-=new
        scan.update(new)

stdout.write(str(cnt))

from itertools import permutations
idx = [i for i in range(1500)]
d = [p for p in permutations(idx,3)]
