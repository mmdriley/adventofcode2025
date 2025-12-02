# N is <s><s>
def is_interesting1(n):
    s = str(n)
    l = len(s)

    if l % 2 != 0:
        return False

    return s[:l//2] == s[l//2:]


# N is <s>{2,}
def is_interesting2(n):
    s = str(n)
    l = len(s)

    for k in range(1, l//2 + 1):
        if l % k != 0:
            continue
        d = l // k

        if s == s[:k] * d:
            return True

    return False


with open('02.txt') as f:
    contents = f.read().strip()

total1 = 0
total2 = 0

for r in contents.split(','):
    start, end = [int(x) for x in r.split('-')]
    for i in range(start, end + 1):
        if is_interesting1(i):
            total1 += i
            total2 += i
        elif is_interesting2(i):
            total2 += i

print(total1)
print(total2)
