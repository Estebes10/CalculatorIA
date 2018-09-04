import fileinput

total = 0

for line in fileinput.input():
    num = int(line)
    total = total + num

print(total)
