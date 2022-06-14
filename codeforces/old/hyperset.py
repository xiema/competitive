from sys import stdin

n,k = map(int, stdin.readline().split())
cards = []
s,e,t = [],[],[]
for _ in range(n):
    c = stdin.readline().strip()
    cards.append(c)
    seen[c] = set()

c = {
    ('S','E'):'T',('E','S'):'T',
    ('S','T'):'E',('T','S'):'E',
    ('E','T'):'S',('T','E'):'S',
}
def match(a, b):
    ret = []
    for i in range(k):
        if a[i] == b[i]:
            ret.append(a[i])
        else:
            ret.append(c[(a[i],b[i])])
    return ''.join(ret)

count = 0
for i in range(n):
    for j in range(i+1,n):
        if cards[j] not in seen[cards[i]]:
            m = match(cards[i],cards[j])
            if m in cards:
                count+=1
                seen[cards[i]].add(m)
                seen[cards[j]].add(m)

print(count)
