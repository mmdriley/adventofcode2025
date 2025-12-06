with open('06.txt') as f:
    contents = [l.strip('\n') for l in f.readlines()]  # explicit argument to strip() so we keep trailing spaces

ops = contents[-1].split()
numberlines = [[int(n) for n in l.split()] for l in contents[:-1]]

# part 1
total = 0
for i, op in enumerate(ops):
    if op == '+':
        n = 0
        for l in numberlines:
            n += l[i]
    else:
        assert op == '*'
        n = 1
        for l in numberlines:
            n *= l[i]

    total += n

print(total)

# part 2
total = 0
contents = [l[::-1] for l in contents]  # reverse each line

total = 0
current_sum = 0
current_product = 1

for i, op in enumerate(contents[-1]):
    n = 0
    for c in contents[:-1]:
        if c[i] == ' ':
            continue
        n = n * 10 + int(c[i])

    if n == 0:
        # column of spaces
        assert op == ' '
        continue

    current_sum += n
    current_product *= n

    if op == '+':
        total += current_sum
    elif op == '*':
        total += current_product
    else:
        continue

    current_sum = 0
    current_product = 1

print(total)
