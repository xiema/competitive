from sys import stdin, stdout

T = int(stdin.readline())
out = []

for _ in range(T):
    r,c = map(int, stdin.readline().split())
    rows = [stdin.readline() for _ in range(r)]
    columns = []
    for i in range(c):
        columns.append(''.join(row[i] for row in rows))

    b = True
    for row in rows:
        if 'P' in row:
            b = False
            break
    if b:
        out.append("0\n")
        continue

    if 'P' not in rows[0] or 'P' not in rows[r-1] or 'P' not in columns[0] or 'P' not in columns[c-1]:
        out.append("1\n")
        continue

    if rows[0][0] == 'A' or rows[r-1][0] == 'A' or rows[0][c-1] == 'A' or rows[r-1][c-1] == 'A':
        out.append("2\n")
        continue
    else:
        b = False
        for i in range(1,r-1):
            if 'P' not in rows[i]:
                b = True
                break
        if b:
            out.append("2\n")
            continue
        for i in range(1,c-1):
            if 'P' not in columns[i]:
                b = True
                break
        if b:
            out.append("2\n")
            continue

    if 'A' in rows[0] or 'A' in rows[r-1] or 'A' in columns[0] or 'A' in columns[c-1]:
        out.append("3\n")
        continue

    b = False
    for row in rows:
        if 'A' in row:
            b = True
            break
    if b:
        out.append("4\n")
    else:
        out.append("MORTAL\n")

stdout.writelines(out)
