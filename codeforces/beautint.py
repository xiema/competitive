from sys import stdin, stdout

n,k = map(int, stdin.readline().split())
digits = list(map(int, stdin.readline().strip()))
add = 0
inc = False
i = 0
while i < n-k:
    if digits[i] > digits[i+k]:
        digits[i+k] = digits[i]
        inc = True
    elif digits[i] < digits[i+k]:
        if not inc:
            for j in range(k-1,-1,-1):
                digits[j] = (digits[j]+1)%10
                ofs = k
                while j+ofs <= i-1+k:
                    digits[j+ofs] = digits[j]
                    ofs+=k
                if digits[j] != 0:
                    break
            inc = True
        digits[i+k] = digits[i]

    i+=1

stdout.write("{}\n".format(len(digits)))
stdout.write(''.join(list(map(str, digits))))
