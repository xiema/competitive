from sys import stdin, stdout

n = int(stdin.readline().strip())
s = list(stdin.readline().strip())

moves = []
d = s[0]
i = 0
flip = False
while i < len(s):
    if flip:
        if s[i] == d:
            moves.append(str(i))
        else:
            flip = False
    else:
        if s[i] != d:
            moves.append(str(i))
            flip = True
    i+=1

if len(moves) == 0:
    stdout.write("0")
elif flip:
    stdout.write("-1")
else:
    stdout.write("{}\n".format(len(moves)))
    stdout.write(' '.join(moves))
