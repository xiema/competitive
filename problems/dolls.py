T = int(input())
out = []

for _ in range(T):
    c = int(input())*2
    s = list(map(int, input().split()))
    dolls = []
    for i in range(0,c,2):
        dolls.append([s[i], s[i+1]])
    dolls.sort(key= lambda x: (-x[0], x[1]))
    stacks = []
    for d in dolls:
        b = False
        for s in stacks:
            if s[0] > d[0] and s[1] > d[1]:
                b = True
                s[0], s[1] = d[0], d[1]
                break
        if not b:
            stacks.append(d)

    out.append(str(len(stacks)))


print("\n".join(out))
