def area(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return abs(x1 - x2 + 1) * abs(y1 - y2 + 1)

red_tiles: list[tuple[int, int]] = []
with open('09.txt') as f:
    for l in f:
        x, y = [int(n) for n in l.split(',')]
        red_tiles.append((x, y))

max_area1 = 0
for i, c1 in enumerate(red_tiles):
    for c2 in red_tiles[i+1:]:
        this_area = area(c1, c2)
        max_area1 = max(max_area1, this_area)

print(max_area1)
