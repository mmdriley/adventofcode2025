ranges: list[tuple[int, int]] = []
within = 0

with open('05.txt') as f:
    for l in f:
        l = l.strip()
        if not l:
            break
        begin, end = [int(x) for x in l.split('-')]
        ranges.append((begin, end))

    for l in f:
        n = int(l.strip())
        for begin, end in ranges:
            if n >= begin and n <= end:
                within += 1
                break
# part 1
print(within)

# sort ranges by start
ranges = sorted(ranges, key=lambda x: x[0])

# combine overlapping ranges
i = 0
while i + 1 < len(ranges):
    begin1, end1 = ranges[i]
    begin2, end2 = ranges[i+1]

    if begin2 <= end1:
        ranges[i] = begin1, max(end1, end2)
        del ranges[i+1]
    else:
        i = i + 1

total_fresh = 0
for begin, end in ranges:
    total_fresh += (end - begin + 1)

# part 2
print(total_fresh)
