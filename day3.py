with open("input3.txt", "r") as f:
    lines = [i for i in f.read().splitlines()]

def count(right, down):
    j, result, len_line = 0, 0, len(lines[0])
    for i in range(0, len(lines), down):
        if lines[i][j] == "#":
            result += 1
        j = (j + right) % len_line
    return result

# part 1
print(count(3, 1))

# part 2
print(count(3, 1) * count(1, 1) * count(5, 1) * count(7, 1) * count(1, 2))