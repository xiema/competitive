from sys import stdin

c = int(stdin.readline())

out = []
for line in stdin:
    if line.endswith("po\n"):
        out.append("FILIPINO")
    elif line.endswith("mnida\n"):
        out.append("KOREAN")
    else:
        out.append("JAPANESE")

print('\n'.join(out))
