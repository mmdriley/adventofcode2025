total = 0

# I could parse these from my input, but this was easier.
popcounts = [5, 7, 7, 7, 7, 6]

with open('12.txt') as f:
    for l in f:
        if 'x' not in l:
            continue

        part1, part2 = l.strip('\n').split(': ')
        width, height = [int(x) for x in part1.split('x')]
        counts = [int(x) for x in part2.split(' ')]

        t = sum(c * p for c, p in zip(counts, popcounts))
        if t < width*height:
            total += 1

print(total)
