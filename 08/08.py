from collections import Counter
import math

coord = tuple[int, int, int]

def dist(t1: coord, t2: coord) -> float:
    x1, y1, z1 = t1
    x2, y2, z2 = t2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

box_coords: list[coord] = []
with open('08.txt') as f:
    for l in f:
        x, y, z = [int(n) for n in l.split(',')]
        box_coords.append((x, y, z))

# map boxes @ coords to their current circuit, identified by the "smallest" coordinate in the set
circuits: dict[coord, coord] = dict()

# everything starts off disjoint
for c in box_coords:
    circuits[c] = c

# compute all the pairwise distances and sort
distances: list[tuple[float, coord, coord]] = []

for i, c1 in enumerate(box_coords):
    for c2 in box_coords[i+1:]:
        distances.append((dist(c1, c2), c1, c2))

distances = sorted(distances)

connections = 0
part2_result = 0

for _, c1, c2 in distances:
    connections += 1
    if circuits[c1] == circuits[c2]:
        # already connected to each other
        continue

    x1, _, _ = c1
    x2, _, _ = c2
    part2_result = x1 * x2

    old_circuit = max(circuits[c1], circuits[c2])

    # circuits[C] <= C by invariant
    new_circuit = min(circuits[c1], circuits[c2])

    in_old_circuit = [k for k, v in circuits.items() if v == old_circuit]
    for c in in_old_circuit:
        circuits[c] = new_circuit

    if connections == 1000:
        # part 1
        circuits_counter = Counter(circuits.values())

        result = 1
        for _, n in circuits_counter.most_common(3):
            result *= n
        print(result)

print(part2_result)
