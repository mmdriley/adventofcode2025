with open('07.txt') as f:
    grid = [l.strip('\n') for l in f.readlines()]

grid = [list(l) for l in grid]

paths: dict[tuple[int, int], int] = dict()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        paths[(i,j)] = 0

for j, c in enumerate(grid[0]):
    paths[(0, j)] = 1 if grid[0][j] == 'S' else 0

# propagate beams
for i, l in enumerate(grid[1:], start=1):
    for j, c in enumerate(l):
        if grid[i-1][j] not in ('S', '|'):
            assert paths[(i-1,j)] == 0
            # no beam to propagate
            continue

        assert paths[(i-1,j)] > 0

        if c in ('.', '|'):
            grid[i][j] = '|'
            paths[(i,j)] += paths[(i-1,j)]
        elif c == '^':
            if j - 1 >= 0:
                assert grid[i][j-1] in ('.', '|')
                grid[i][j-1] = '|'
                paths[(i, j-1)] += paths[(i-1,j)]
            if j + 1 < len(grid[i]):
                assert grid[i][j+1] in ('.', '|')
                grid[i][j+1] = '|'
                paths[(i, j+1)] += paths[(i-1,j)]

# count splits
splits = 0
for i in range(1, len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^' and grid[i-1][j] in ('S', '|'):
            splits += 1

print(splits)

total_paths = 0
for j in range(len(grid[0])):
    total_paths += paths[(len(grid)-1, j)]

print(total_paths)
