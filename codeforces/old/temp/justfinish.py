from collections import deque

if __name__ == "__main__":
    T = int(input().strip())
    out = []
    for t in range(T):
        N = int(input().strip())
        plist = list(map(int,input().split()))
        qlist = list(map(int,input().split()))
        trk = deque()
        for i in range(N):
            trk.append(plist[i]-qlist[i])
        i,j = 0,0
        fuel = 0
        while i < N and j < len(trk):
            fuel += trk[j]
            while fuel < 0:
                fuel -= trk[i]
                trk.append(trk[i])
                i+=1
            j+=1
        if i >= N:
            out.append("Case {}: Not possible".format(t+1))
        else:
            out.append("Case {}: Possible from station {}".format(t+1,i+1))
    print('\n'.join(out))
