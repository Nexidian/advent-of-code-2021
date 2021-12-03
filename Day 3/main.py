from typing import List


def load_input() -> List:
    with open('input.txt') as file:
        lines = [line.rstrip() for line in file.readlines()]
    return lines


def first_star(puzzle_input: List):
    count_dict = {}
    gamma = ''
    epsilon = ''
    for line in puzzle_input:
        for i in range(0, len(line)):
            if i in count_dict:
                count_dict[i] += int(line[i])
            else:
                count_dict[i] = int(line[i])
    line_count = len(puzzle_input)
    for i in range(0, len(count_dict)):
        gamma += '1' if count_dict[i] > line_count / 2 else '0'
        epsilon += '1' if not count_dict[i] > line_count / 2 else '0'
    print(int(gamma, 2) * int(epsilon, 2))



if __name__ == "__main__":
    first_star(load_input())

