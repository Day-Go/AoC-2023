with open("input.txt", "r") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    print(line)
    num_str = ''
    for char in line:
        if char.isdigit():
            num_str += char
            break

    for char in line[::-1]:
        if char.isdigit():
            num_str += char
            break

    sum += int(num_str)

print(sum)