floor = 0
count = 0

with open("input.txt") as file:
    for i, ch in enumerate(file.readline()):
        if ch == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            count = i+1
            break
            
print(count)
