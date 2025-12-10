import dataclasses

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

@dataclasses.dataclass
class Machine:
    target_config: list[bool]
    buttons: list[list[int]]
    joltage_targets: list[int]

machines = []

with open('10.txt') as f:
    for l in f:
        pieces = l.strip('\n').split(' ')
        machines.append(Machine(
            target_config=[c == '#' for c in pieces[0].strip('[]')],
            buttons=[[int(x) for x in b.strip('()').split(',')] for b in pieces[1:-1]],
            joltage_targets=[int(x) for x in pieces[-1].strip('{}').split(',')],
        ))

# note: fewest steps to all-off from a config is the same as the fewest steps
# *from* all-off to that config
def fewest_steps_to_all_off(config: list[bool], buttons: list[list[int]]) -> int:
    if all([not x for x in config]):
        return 0
    if len(buttons) == 0:
        return 100_000
    
    # never need to consider the case where we push a button twice, since it's the
    # same as never pushing it at all.
    v1 = fewest_steps_to_all_off(config, buttons[1:])
    config2 = [x for x in config]
    for i in buttons[0]:
        config2[i] = not config2[i]
    v2 = 1 + fewest_steps_to_all_off(config2, buttons[1:])

    return min(v1, v2)


def fewest_presses_to_joltage_config(target: list[int], buttons: list[list[int]]) -> int:
    onehot_lines = []
    for b in buttons:
        coeff_line = [0 for _ in target]
        for i in b:
            coeff_line[i] = 1
        onehot_lines.append(coeff_line)
    onehot_lines = np.array(onehot_lines).transpose()

    # now we want to solve b_n*x_n - target_n = 0,
    # optimizing for minimal sum of x_n
    opt_coefficient_array = np.array([1 for _ in buttons])

    T = np.array(target)

    lc = LinearConstraint(onehot_lines, T, T)
    integrality = np.ones_like(opt_coefficient_array)
    res = milp(c=opt_coefficient_array, constraints=lc, integrality=integrality)
    assert res.success

    return int(res.fun)


# part 1
total_pushes1 = 0
for m in machines:
    total_pushes1 += fewest_steps_to_all_off(m.target_config, m.buttons)
print(total_pushes1)

# part 2
total_pushes2 = 0
for m in machines:
    total_pushes2 += fewest_presses_to_joltage_config(m.joltage_targets, m.buttons)
print(total_pushes2)
