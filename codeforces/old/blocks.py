n = int(input().strip())
blocks = list(input().strip())
c = blocks[0]
cnt = 0
for b in blocks:
    if b == c:
        cnt += 1

if cnt%2 and (n-cnt)%2:
    print(-1)
else:
    moves = []
    if (n-cnt)%2:
        c = 'W' if c == 'B' else 'B'
    for i in range(n-1):
        if blocks[i] != c:
            blocks[i] = c
            blocks[i+1] = 'W' if blocks[i+1] == 'B' else 'B'
            moves.append(str(i+1))
    print(len(moves))
    print(' '.join(moves))
