N = int(input())

step, max_number = 1, 1

while N > max_number:
    step += 1
    max_number = 1 + 6 * (step * (step - 1)) // 2

print(step)