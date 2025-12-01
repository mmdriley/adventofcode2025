with open('01.txt') as f:
    rotations = [l.strip() for l in f if l != '\n']


def endings():
    pos = 50
    for r in rotations:
        if r[0] == 'L':
            pos -= int(r[1:])
        else:
            assert(r[0] == 'R')
            pos += int(r[1:])
        
        pos = pos % 100
        yield pos


def clicks():
    pos = 50
    for r in rotations:
        if r[0] == 'L':
            signum = -1
        else:
            assert(r[0] == 'R')
            signum = 1
        magnitude = int(r[1:])

        for _ in range(magnitude):
            pos = (pos + signum) % 100
            yield pos


print(sum([p == 0 for p in endings()]))
print(sum([p == 0 for p in clicks()]))
