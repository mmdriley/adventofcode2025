total = 0

with open('03.txt') as f:
    for l in f:
        digits = [int(x) for x in l.strip()]

        max_joltage = 0

        for i in range(0, len(digits)):
            for j in range(i + 1, len(digits)):
                joltage = digits[i] * 10 + digits[j]
                max_joltage = max(max_joltage, joltage)
        total += max_joltage

print(total)
