from sys import stdin, stdout

T = int(stdin.readline().strip())

lines = []

for _ in range(T):
    s = stdin.readline().strip()
    c = 0
    pos = []
    i,j = 0,len(s)
    while i < j:
        if s[i:i+5] == "twone":
            c += 1
            pos.append(str(i+3))
            i+=5
        elif s[i:i+3] == "two" or s[i:i+3] == "one":
            c += 1
            pos.append(str(i+2))
            i+=3
        else:
            i+=1

    lines.append("{}\n".format(c))
    lines.append(" ".join(pos) + '\n')

stdout.writelines(lines)
