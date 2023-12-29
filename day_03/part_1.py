x = 0
y = 0
vis = set()
vis.add((0, 0))

with open("input.txt", "r") as file:
    dir = file.readline()

for ch in dir:
    match ch:
        case '<':
            x -= 1
        case '>':
            x += 1
        case '^':
            y += 1
        case 'v':
            y -= 1
    vis.add((x, y))
    
print(len(vis))
