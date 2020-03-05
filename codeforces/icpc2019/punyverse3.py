from sys import stdin, stdout
from collections import deque

class Node:
    def __init__ (self, idx, weight):
        self.idx = idx
        self.weight = weight
        self.neighbors = []
        self.degree = 0

    def addneighbor (self, node):
        self.neighbors.append(node)
        self.degree += 1
        node.neighbors.append(self)
        node.degree += 1

    def trim (self):
        other = self.neighbors[0]
        if (self.weight > 0 and other.weight > 0) or (self.weight < 0 and other.weight < 0):
            self.weight = other.weight
            self.neighbors = other.neighbors
            self.degree = other.degree - 1
            self.neighbors.remove(self)


T = int(stdin.readline())

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

    nodes = {}
    nodes[root] = Node(root, weights[root])
    root = nodes[root]
    ordered, next = deque(), deque([root])
    losingnodes = set()
    ends = []
    visited = set()
    while next:
        v1 = next.popleft()
        visited.add(v1.idx)
        c = 0
        for v2 in filter(lambda x : x not in visited, segs[v1.idx]):
            nodes[v2] = node = Node(v2, weights[v2])
            v1.addneighbor(node)
            next.append(node)
            c += 1
            #ordered.appendleft((v2, v1))
        if c == 0:
            ends.append(node)

    for node in ends:
        node.trim()
