from itertools import combinations

with open("input1.txt", "r") as f:
    numbers = list(map(int, [i for i in f.read().splitlines()]))

# part 1
lookup = set()
for i in numbers:
    complement = 2020 - i
    if complement in lookup:
        print(complement * i)
        break
    else:
        lookup.add(i)
        
# part 2
for (i, j, k) in set(combinations(numbers, 3)):
    if i + j + k == 2020:
        print(i * j * k)