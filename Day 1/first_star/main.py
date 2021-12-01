def solve():
    increases = 0
    with open('input.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i - 1]):
            increases += 1
    print(increases)


if __name__ == "__main__":
    solve()
