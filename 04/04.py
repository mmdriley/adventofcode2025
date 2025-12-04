grid = []

with open('04.txt') as f:
    for l in f:
        l = l.strip()
        if not l:
            continue
        grid.append(list(l))

# pad the border with spaces
grid = [[' '] + l + [' '] for l in grid]
pad = [' '] * len(grid[0])
grid = [pad] + grid + [pad]


adjacencies = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1),
]


def remove_round(grid: list[list[str]]) -> int:
    removed = []

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] != '@':
                continue

            present = 0
            for di, dj in adjacencies:
                if grid[i + di][j + dj] == '@':
                    present += 1
            if present < 4:
                removed.append((i, j))
    
    for i, j in removed:
        grid[i][j] = '.'

    return len(removed)


# part 1
n = remove_round(grid)
print(n)

# part 2
while True:
    r = remove_round(grid)
    n += r
    if r == 0:
        break

print(n)
