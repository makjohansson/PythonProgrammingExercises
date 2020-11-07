import random


def move_up(y):
    return y + 1


def move_down(y):
    return y - 1


def move_left(x):
    return x - 1


def move_right(x):
    return x + 1


def walk(index, x, y):
    switch = {
        1: move_up(y),
        2: move_down(y),
        3: move_left(x),
        4: move_right(x)
    }
    if step <= 2:
        return x, switch.get(index)
    else:
        return switch.get(index), y


def out_of_bounds(limit, x, y):
    if (x or y) > limit:
        return True
    if (x or y) < (limit * - 1):
        return True
    else:
        return False


def reset():
    return 0.0, 0.0


def in_percent(share, hole):
    return round((share / hole) * 100, 2)


boundary = int(input("Enter the size: "))
num_of_steps = int(input("Enter the number of steps: "))
number_of_sailors = int(input("Enter number of sailors: "))
counter = number_of_sailors
x_pos, y_pos = reset()
sailor_fell = False
num_of_sailors_in_the_water = 0

while counter > 0:
    for i in range(num_of_steps):
        step = random.randint(1, 4)
        x_pos, y_pos = walk(step, x_pos, y_pos)
        if out_of_bounds(boundary, x_pos, y_pos):
            sailor_fell = True
            break

    if sailor_feel:
        num_of_sailors_in_the_water += 1
        sailor_feel = False
    counter -= 1
    x_pos, y_pos = reset()

print(f"\nOut of {number_of_sailors}, {num_of_sailors_in_the_water} "
      f"({in_percent(num_of_sailors_in_the_water, number_of_sailors)}%) fell into the water.")





