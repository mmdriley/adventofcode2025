from collections import defaultdict

with open('07.txt') as f:
    grid = [l.strip('\n') for l in f.readlines()]

grid = [list(l) for l in grid]


splitters_hit: set[tuple[int, int]] = set()
paths: dict[tuple[int, int], int] = defaultdict(int)
for j, c in enumerate(grid[0]):
    if c == 'S':
        paths[(0,j)] = 1


# propagate beams
for i, l in enumerate(grid[1:], start=1):
    for j, c in enumerate(l):
        if paths[(i-1,j)] == 0:
            # no incoming beam, nothing to do
            continue

        if c == '.':
            paths[(i,j)] += paths[(i-1,j)]
        elif c == '^':
            splitters_hit.add((i, j))
            if j - 1 >= 0:
                assert grid[i][j-1] == '.'
                paths[(i, j-1)] += paths[(i-1,j)]
            if j + 1 < len(grid[i]):
                assert grid[i][j+1] == '.'
                paths[(i, j+1)] += paths[(i-1,j)]

# part 1
print(len(splitters_hit))

# part 2
total_paths = 0
for j in range(len(grid[0])):
    total_paths += paths[(len(grid)-1, j)]

print(total_paths)
