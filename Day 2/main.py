from typing import List


def load_input() -> List:
    lines = []
    with open('input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def first_star(input: List):
    horizontal, depth = 0, 0
    for line in input:
        direction, amount = line.split()
        amount = int(amount)
        match direction:
            case 'forward':
                horizontal += amount
            case 'down':
                depth += amount
            case 'up':
                depth -= amount
            case _:
                pass
    print(horizontal * depth)


def second_star(input: List):
    horizontal, depth, aim = 0, 0, 0
    for line in input:
        direction, amount = line.split()
        amount = int(amount)
        match direction:
            case 'forward':
                horizontal += amount
                depth += (aim * amount)
            case 'down':
                aim += amount
            case 'up':
                aim -= amount
            case _:
                pass
    print(horizontal * depth)


if __name__ == "__main__":
    data = load_input()
    first_star(data)
    second_star(data)
