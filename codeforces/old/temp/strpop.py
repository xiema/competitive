from sys import stdin,stdout

def check(s):
    if len(s) == 0:
        return True
    i,j,c = 0,1,s[0]
    while j < len(s):
        if s[j] != c:
            if j-i>1 and check(s[:i]+s[j:]):
                return True
            i,c = j,s[j]
        j+=1
    else:
        if j-i>1 and check(s[:i]):
            return True
    return False

T = int(stdin.readline().strip())
for _ in range(T):
    s = stdin.readline().strip()
    if check(s):
        stdout.write("1\n")
    else:
        stdout.write("0\n")
