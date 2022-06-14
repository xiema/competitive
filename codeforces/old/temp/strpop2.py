from sys import stdin,stdout

def check(grp):
    if len(grp) == 0:
        return True
    if int(grp) == 0:
        return False
    if '0' not in grp:
        return True
    if len(grp)%2 and grp[len(grp)//2] == '1':
        return True

    i=1
    while i<len(grp)-1:
        if grp[i]=='1':
            a = grp[:i-1] if i-1>0 else ''
            b = grp[i+2:] if i+2<len(grp) else ''
            if check(a+'1'+b):
                return True
        i+=1
    return False

T = int(stdin.readline().strip())
for _ in range(T):
    s = stdin.readline().strip()
    i,j,c = 0,1,s[0]
    grp = []
    while j<len(s):
        if s[j] != c:
            grp.append('1' if j-i>1 else '0')
            i,c = j,s[j]
        j+=1
    else:
        grp.append('1' if j-i>1 else '0')

    if check(''.join(grp)):
        stdout.write("1\n")
    else:
        stdout.write("0\n")
