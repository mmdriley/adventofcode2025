def area(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

red_tiles: list[tuple[int, int]] = []
with open('09.txt') as f:
    i = 0
    for l in f:
        x, y = [int(n) for n in l.split(',')]
        red_tiles.append((x, y))

rects_with_areas = []
for i, c1 in enumerate(red_tiles):
    for c2 in red_tiles[i+1:]:
        rects_with_areas.append((c1, c2, area(c1, c2)))

rects_with_areas = sorted(rects_with_areas, key=lambda x: x[2], reverse=True)

# part 1
print(rects_with_areas[0][2])

# if you have a box and no segments intersect it, you win. (equality matters)

h_segments = []
v_segments = []

red_tiles_wrapped = red_tiles + [red_tiles[0]]
for c1, c2 in zip(red_tiles_wrapped, red_tiles_wrapped[1:]):
    c1x, c1y = c1
    c2x, c2y = c2

    if c1x == c2x:
        v_segments.append((c1, c2))
    else:
        assert c1y == c2y
        h_segments.append((c1, c2))

# add some artifical segments to reflect boundaries

for x, y in red_tiles:
    if x < 40_000:
        h_segments.append(((0, y), (x * 3 // 5, y)))
    if x > 60_000:
        h_segments.append(((x * 7 // 5, y), (100_000, y)))
    if y < 40_000:
        v_segments.append(((x, 0), (x, y * 3 // 5)))
    if y > 60_000:
        v_segments.append(((x, y * 7 // 5), (x, 100_000)))

# find the largest rectangle that doesn't intersect any segment

max_c1, max_c2, max_area = None, None, None

for c1, c2, a in rects_with_areas:
    c1x, c1y = c1
    c2x, c2y = c2

    left = min(c1x, c2x)
    right = max(c1x, c2x)

    bottom = min(c1y, c2y)
    top = max(c1y, c2y)

    def v_segment_crossings():
        for p1, p2 in v_segments:
            p1x, p1y = p1
            p2x, p2y = p2
            assert p1x == p2x

            if p1x <= left or p1x >= right:
                continue

            if p1y < top and p2y > top:
                return True
            if p2y < top and p1y > top:
                return True
            if p1y < bottom and p2y > bottom:
                return True
            if p2y < bottom and p1y > bottom:
                return True
        return False

    def h_segment_crossings():
        for p1, p2 in h_segments:
            p1x, p1y = p1
            p2x, p2y = p2
            assert p1y == p2y

            if p1y <= bottom or p1y >= top:
                continue

            if p1x < left and p2x > left:
                return True
            if p2x < left and p1x > left:
                return True
            if p1x < right and p2x > right:
                return True
            if p2x < right and p1x > right:
                return True
        return False

    if v_segment_crossings() or h_segment_crossings():
        continue

    assert a == area(c1, c2)
    max_c1, max_c2, max_area = c1, c2, area(c1, c2)
    break

print(max_area)

# some useful code to plot the data and arrived-upon rectangle
# import numpy as np
# import matplotlib.pyplot as plt

# x_coords = [x for x, _ in red_tiles]
# y_coords = [y for _, y in red_tiles]

# plt.plot(x_coords, y_coords)

# l = [max_c1, max_c2]
# x_coords = [x for x, _ in l]
# y_coords = [y for _, y in l]

# plt.plot(x_coords, y_coords)

# plt.show()
