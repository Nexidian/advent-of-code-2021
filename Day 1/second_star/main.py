def solve():
    increases = 0
    previous_sum = 0
    n = 3
    with open('input.txt') as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]
    for i in range(len(lines) - n):
        sum_of_window = sum(lines[i:i+n])
        if sum_of_window > previous_sum:
            increases += 1
        previous_sum = sum_of_window
    print(increases)


if __name__ == "__main__":
    solve()
