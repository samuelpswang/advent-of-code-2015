import json

obj = []
with open("input.txt", "r") as file:
    obj = json.load(file)

total = 0
queue = [obj]
while queue: 
    curr = queue.pop()
    if type(curr) == dict:
        have_red = False
        buffer = []
        for key, item in curr.items():
            buffer.append(item)
            if item == "red":
                have_red = True
                break
        if not have_red:
            queue.append(buffer)
    elif type(curr) == list:
        for item in curr:
            queue.append(item)
    elif type(curr) == int:
        total += curr

print(total)
