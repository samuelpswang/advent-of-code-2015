import json

obj = []
with open("input.txt", "r") as file:
    obj = json.load(file)

total = 0
queue = [obj]
while queue: 
    curr = queue.pop()
    if type(curr) == dict:
        for key, item in curr.items():
            queue.append(item)
    elif type(curr) == list:
        for item in curr:
            queue.append(item)
    elif type(curr) == int:
        total += curr

print(total)
