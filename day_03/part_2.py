x = y = 0
rx = ry = 0
vis = set()
vis.add((0, 0))
is_santa = True

with open("input.txt", "r") as file:
    dir = file.readline()

for ch in dir:
    match ch:
        case '<':
            if is_santa: x -= 1
            else: rx -= 1
        case '>':
            if is_santa: x += 1
            else: rx += 1
        case '^':
            if is_santa: y += 1
            else: ry += 1
        case 'v':
            if is_santa: y -= 1
            else: ry -= 1
    if is_santa: vis.add((x, y))
    else: vis.add((rx, ry))
    is_santa = not is_santa

print(len(vis))
