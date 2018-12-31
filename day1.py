with open("input1.txt", "r") as input_file:
    input = input_file.readlines()

inputs = [int(i.strip()) for i in input]

freq = 0
for input in inputs:
    freq += input
print(freq)
