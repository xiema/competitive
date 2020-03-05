from sys import stdin, stdout
from collections import deque

T = int(stdin.readline())

class Tree:
    __slots__ = ['sizes', 'total']
    def __init__ (self, sizes, total):
        self.sizes = sizes
        self.total = total

    def getbest (self):
        val, idx = None, None
        for (i,sz) in enumerate(self.sizes):
            (v1,v2,t) = sz
            _val = abs(t - self.total)
            if not val or _val < val:
                val, idx = _val, i
        return val, idx

    def split (self, idx):
        new = Tree(self.sizes[idx+1:], self.total-self.sizes[idx][2])
        self.total = self.sizes[idx][2]
        del self.sizes[idx:]
        return new

    def __repr__ (self):
        return str(self.total)


for _ in range(T):
    n, m = map(int, stdin.readline().split())
    b = [-int(x) for x in stdin.readline().split()]
    w = map(int, stdin.readline().split())
    weights = {k : v for k,v in zip(range(1,n+1), map(sum,zip(b,w)))}
    total = sum(weights.values())
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

    ordered, next = deque(), deque([root])
    visited = set()
    while next:
        v1 = next.popleft()
        visited.add(v1)
        for v2 in filter(lambda x : x not in visited, segs[v1]):
            next.append(v2)
            ordered.appendleft((v2, v1))

    acc = weights.copy()
    sizes = []
    for v1,v2 in ordered:
        wt = acc[v1]
        sizes.append((v1, v2, wt))
        acc[v2] += wt

    print(sizes)
    print(total+)

    trees = [Tree(sizes, total)]
    for _ in range(m-1):
        v,i,tree = None, None, None
        for _tree in trees:
            if _tree.sizes:
                _v,_i = _tree.getbest()
                if not v or _v < v:
                    v,i,tree = _v,_i,_tree
        trees.append(tree.split(i))
        print(trees)
