with open('07.txt') as f:
    grid = [l.strip('\n') for l in f.readlines()]

grid = [list(l) for l in grid]

# propagate beams
for i, l in enumerate(grid):
    if i == 0:
        continue

    for j, c in enumerate(l):
        if grid[i-1][j] not in ('S', '|'):
            # no beam to propagate
            continue
        
        if c == '.':
            grid[i][j] = '|'
        elif c == '^':
            if j - 1 >= 0:
                assert grid[i][j-1] in ('.', '|')
                grid[i][j-1] = '|'
            if j + 1 < len(grid[i]):
                assert grid[i][j+1] in ('.', '|')
                grid[i][j+1] = '|'

# count splits
splits = 0
for i in range(1, len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '^' and grid[i-1][j] in ('S', '|'):
            splits += 1

print(splits)
