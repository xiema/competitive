from sys import stdin,stdout

t = int(stdin.readline().strip())

for _ in range(t):
    s = stdin.readline().strip()
    counts = {'L':0,'R':0,'U':0,'D':0}
    for c in s:
        counts[c]+=1
    counts['L'] = counts['R'] = min(counts['L'],counts['R'])
    counts['U'] = counts['D'] = min(counts['D'],counts['U'])

    if counts['L'] == 0 and counts['U'] > 0:
        counts['U'] = counts['D'] = 1
    elif counts['U'] == 0 and counts['L'] > 0:
        counts['L'] = counts['R'] = 1

    stdout.write('{}\n'.format(sum(counts.values())))
    inst = ""
    inst += counts['L'] * 'L'
    inst += counts['U'] * 'U'
    inst += counts['R'] * 'R'
    inst += counts['D'] * 'D'
    stdout.write(inst + '\n')
