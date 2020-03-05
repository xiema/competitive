from sys import stdin,stdout
from itertools import permutations

memo_perm = {}
memo_perm_zero = {}

def permwithsum (sum, i, zero=False):
    if (sum, i) in memo_perm:
        if zero:
            return memo_perm_zero[(sum,i)]
        else:
            return memo_perm[(sum,i)]
    else:
        perms, perms_zero = [], None
        if i == 2:
            x = sum//2
            y = sum-x
            while x > 0:
                if x != y:
                    perms.extend([(x, y), (y, x)])
                    perms_zero.extend([(x, y), (y, x)])
                else:
                    perms.append((x, y))
                x -= 1
                y += 1
            perms_zero = perms + [(sum, 0), (0, sum)]
        else:
            for x in range(sum-i+1,0,-1):
                perms.extend([tuple([x, *suf]) for suf in permwithsum(sum-x, i-1)])
            for suf in permwithsum(sum, i-1):
                perms_zero.extend([tuple([0, *suf]), tuple([*suf, 0])])
        return memo_perm.setdefault((sum, i), perms)

class Node:
    def __init__ (self, idx):
        self.idx = idx
        self.parent = None
        self.children = []
        self.childcount = 0
        self.memo = {}
        self.sizeL = 0
        self.sizeR = 0

    def getoptimal (self, n):
        try:
            return self.memo[n]
        except KeyError:
            r = 0
            #this in left group
            if self.childcount < n:
                for ns in permwithsum(n, min(self.sizeR,n-self.childcount)):
                    total = 0
                    for i,v in enumerate(ns):
                        if v > self.children[i].sizeR:
                            total = 0
                            break
                        else:
                            total += self.children[i].getoptimal(v)
                    r = max(r, total)
            else:
                for ns in permwithsum(n,
            #this in one of right groups
            #for i in range(max(1,n-self.childcount), min(n, sizeR)):


T = int(stdin.readline())

for _ in range(T):
    n,m = map(int, stdin.readline().split())
    b = [-int(x) for x in stdin.readline().split()]
    w = map(int, stdin.readline().split())
    votes = {k : v for k,v in zip(range(1,n+1), map(sum, zip(b,w)))}
    segs = {}
    root = None
    for _ in range(n-1):
        a, b = map(int, stdin.readline().split())
        if a not in segs:
            segs[a] = [b]
            root = a
        else:
            segs[a].append(b)
        if b not in segs:
            segs[b] = [a]
            root = b
        else:
            segs[b].append(a)

    print(permwithsum(9,4))
