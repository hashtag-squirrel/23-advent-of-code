# Read file and split into lines
file = open('day01/input.txt', 'r')
lines = file.readlines()

# declare count as 0
count = 0

words = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

replacements = [
    'o1e',
    't2o',
    't3ree',
    'f4ur',
    'f5ve',
    's6x',
    's7ven',
    'e8ght',
    'n9ne'
]

# iterate over lines
for line in lines:
    for i in range(len(words)):
        if words[i] in line:
            line = line.replace(words[i], replacements[i])

    all_numbers = []
    for char in line:
        if char.isnumeric():
            all_numbers.append(char)
    print(all_numbers)
    number_to_add = all_numbers[0] + all_numbers[-1]

    count += int(number_to_add)

# print total count
print(count)
