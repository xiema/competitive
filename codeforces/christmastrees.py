from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
treepos = list(map(int, stdin.readline().split()))
treepos.sort()
treespaces = []

spacecounts = {}
for i in range(n-1):
    spaces = treepos[i+1]-treepos[i]-1
    if spaces:
        spacecounts[spaces] = spacecounts.setdefault(spaces,0) + 1
        treespaces.append((spaces, treepos[i], treepos[i+1]))
treespaces.sort()
treespaces.append((-1, treepos[-1], treepos[0]))

people = []
total = 0
dist, i, c, count = 0, 0, len(treespaces), 0
while count < m:
    dist += 1
    for j in range(i,c):
        a,b = treespaces[j][1]+dist, treespaces[j][2]-dist
        people.append(a)
        if a != b:
            total+=2*dist
            people.append(b)
            count += 2
            if a+1 == b:
                i = j+1
        else:
            total+=dist
            count += 1
            i = j+1

rem = count-m
total -= dist*rem

stdout.write('{}\n'.format(total))
stdout.write(' '.join(map(str, people[0:m])))
