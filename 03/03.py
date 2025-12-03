import functools

@functools.cache
def max_joltage(digits: str, n: int) -> int:
    if n == 0 or len(digits) == 0 or n > len(digits):
        return 0

    v1 = int(digits[0]) * 10 ** (n - 1) + max_joltage(digits[1:], n - 1)
    v2 = max_joltage(digits[1:], n)

    return max(v1, v2)


total1 = 0
total2 = 0

with open('03.txt') as f:
    for l in f:
        digits = l.strip()

        total1 += max_joltage(digits, 2)
        total2 += max_joltage(digits, 12)

print(total1)
print(total2)
