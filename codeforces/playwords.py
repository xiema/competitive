from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    words = {"01" : set(), "10" : set(), "00" : set(), "11" : set()}
    indices = {}
    for i in range(1,n+1):
        w = stdin.readline().strip()
        words[w[0]+w[-1]].add(w)
        indices[w] = i

    if words["00"] and words["11"]:
        if not words["01"] and not words["10"]:
            stdout.write("-1\n")
            continue

    ans = []
    wa,wb = words["01"],words["10"]
    if len(wb) > len(wa):
        wa,wb = wb,wa
    diff = len(wa)-len(wb)
    if diff > 1:
        revwb = set(w[::-1] for w in wb)
        avail = wa-revwb
        if len(avail) < diff-1:
            stdout.write("-1\n")
            continue
        else:
            while diff > 1:
                w = avail.pop()
                ans.append(str(indices[w]))
                diff-=2
    stdout.write("{}\n".format(len(ans)))
    stdout.write(' '.join(ans) + '\n')
