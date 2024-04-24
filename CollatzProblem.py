def collatz_steps(num):
    steps = 0
    x = num
    
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        steps += 1

    return steps

number = int(input("Enter number: "))

steps = collatz_steps(number)
print(f"Number of steps to reach 1 from {number} is: {steps}")
