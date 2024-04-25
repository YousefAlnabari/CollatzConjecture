for m in range(1, 51):
    x = m
    steps = 0
    print(f"Starting with {x}:")

    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        steps += 1
        print(f"Steps {steps}: {x}")
    
    if steps == 111:
        print(f"The number {m} takes 111 steps to reach 1.")
