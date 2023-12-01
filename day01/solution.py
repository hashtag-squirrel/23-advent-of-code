# Read file and split into lines
file = open('day01/example.txt', 'r')
lines = file.readlines()

# declare count as 0
count = 0

# list of number words
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

# list of number words containing the number
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
    # replace number words with replacements
    for i in range(len(words)):
        if words[i] in line:
            line = line.replace(words[i], replacements[i])

    # add numbers in line to list
    all_numbers = [char for char in line if char.isnumeric()]

    # concatenate first and last number in list
    number_to_add = all_numbers[0] + all_numbers[-1]

    # add number to total count
    count += int(number_to_add)

# print total count
print(count)
