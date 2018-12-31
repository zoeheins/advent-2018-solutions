with open("input2.txt", "r") as input_file:
    inputs = input_file.readlines()


two_letters = 0
three_letters = 0
ids = [i.strip() for i in inputs]

for id in ids:
    letters = list(set(id))
    letters.sort()  # sort alphabetically
    letters = "".join(letters)  # revert back to string

    for letter in letters:
        count = id.count(letter)
        if count == 2:
            two_letters += 1
            break

    for letter in letters:
        count = id.count(letter)
        if count == 3:
            three_letters += 1
            break

print(two_letters * three_letters)
