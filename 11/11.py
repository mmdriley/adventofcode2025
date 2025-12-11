from functools import cache

ins_outs: dict[str, list[str]] = dict()

with open('11.txt') as f:
    for l in f:
        node, outputs = l.strip('\n').split(': ', 2)
        outputs = outputs.split(' ')

        ins_outs[node] = outputs

ins_outs['out'] = []

@cache
def paths(v1: str, v2: str) -> int:
    if v1 == v2:
        return 1
    
    outs = ins_outs[v1]
    if len(outs) == 0:
        return 0
    
    r = 0
    for o in outs:
        r += paths(o, v2)
    return r

# part 1
print(paths('you', 'out'))

# part 2
first, second = 'dac', 'fft'
if paths(first, second) == 0:
    first, second = second, first

print(paths('svr', first) * paths(first, second) * paths(second, 'out'))
