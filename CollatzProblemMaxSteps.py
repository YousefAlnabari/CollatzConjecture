max_steps = 0
number_with_max_steps = 0

for m in range(1, 51):
    x = m
    steps = 0

    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        steps += 1

    if steps > max_steps:
        max_steps = steps
        number_with_max_steps = m

print(f"The number {number_with_max_steps} takes the most steps ({max_steps} steps) to reach 1.")
