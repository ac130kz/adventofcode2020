with open("input2.txt", "r") as f:
    # 17-20 x: zsxjrxkgxxxxxxxmxgxf
    lines = []
    for i in f.read().splitlines():
        (two_numbs, char, password) = i.split()
        lo, hi = tuple(map(int, two_numbs.split("-")))
        lines.append((lo, hi, char[0], password))
        
# part 1
valid = 0
for (lo, hi, char, password) in lines:
    occured = 0
    for c in password:
        if c == char:
            occured += 1
    if lo <= occured <= hi:
        valid += 1
print(valid)

# part 2
valid = 0
for (lo, hi, char, password) in lines:
    if (password[lo - 1] == char) != (password[hi - 1] == char):
        valid += 1
print(valid)