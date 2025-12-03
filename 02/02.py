import math


def repeated_numbers(limit):
    r = set()
    max_len = math.floor(math.log10(limit) + 1)

    for i in range(1, 10 ** (max_len // 2)):
        width = math.floor(math.log10(i) + 1)
        stride = 10 ** width

        n = stride * i + i
        while n <= limit:
            r.add(n)
            n = stride * n + i

    return r


# N is <s><s>
def is_interesting1(n):
    if n not in repeated:
        return False

    s = str(n)
    l = len(s)

    if l % 2 != 0:
        return False

    return s[:l//2] == s[l//2:]


with open('02.txt') as f:
    contents = f.read().strip()

max_n = 0
for r in contents.split(','):
    start, end = [int(x) for x in r.split('-')]
    max_n = max(max_n, start, end)

repeated = repeated_numbers(max_n)

total1 = 0
total2 = 0

for r in contents.split(','):
    start, end = [int(x) for x in r.split('-')]
    for i in range(start, end + 1):
        if i in repeated:
            total2 += i

            if is_interesting1(i):
                total1 += i

print(total1)
print(total2)
