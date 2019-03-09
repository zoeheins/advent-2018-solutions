import re


with open("input3.txt", "r") as input_file:
    inputs = input_file.readlines()

claims = [i.strip() for i in inputs]
fabric = [[0 for x in range(1000)] for y in range(1000)]

for claim in claims:
    groups = re.search(r"#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)", claim).groups()
    id, left, top, width, height = [int(g) for g in groups]

    bottom = top + height
    right = left + width
    for row in range(top, bottom):
        for col in range(left, right):
            fabric[row][col] += 1

total = 0
for row in fabric:
    for claim in row:
        if claim >= 2:
            total += 1

print(total)
