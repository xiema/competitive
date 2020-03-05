from sys import stdin,stdout

def check(s, a,b, si=0,ai=0,bi=0):
    if ai >= len(a) and bi >= len(b):
        return True
    if ai < len(a):
        i=si
        while i < len(s):
            if s[i] == a[ai]:
                if check(s,a,b,i+1,ai+1,bi):
                    return True
                else:
                    break
            i+=1
    if bi < len(b):
        i=si
        while i < len(s):
            if s[i] == b[bi]:
                if check(s,a,b,i+1,ai,bi+1):
                    return True
                else:
                    break
            i+=1
    return False


T = int(stdin.readline().strip())
for _ in range(T):
    s = stdin.readline().strip()
    t = stdin.readline().strip()
    possible = False
    for i in range(0,len(t)):
        if check(s,t[:i],t[i:]):
            possible = True
            break
    stdout.write(["NO\n","YES\n"][possible])
