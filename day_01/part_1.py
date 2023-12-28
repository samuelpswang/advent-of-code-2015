floor = 0

with open("input.txt") as file:
    for ch in file.readline():
        if ch == '(':
            floor += 1
        else:
            floor -= 1

print(floor)
