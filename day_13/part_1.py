from itertools import permutations

costs = {}
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n").strip(".")
        line = line.split(" ")
        name1 = line[0]
        name2 = line[-1]
        val = int(line[3])
        if "lose" in line:
            val *= -1
        if name1 not in costs:
            costs[name1] = {}
        costs[name1][name2] = val

guests = [key for key in costs]
perms = permutations(guests)

max_happiness = 0
for perm in perms:
    curr = 0
    for i in range(len(perm)-1):
        curr += costs[perm[i]][perm[i+1]]
    curr += costs[perm[-1]][perm[0]]
    for i in range(len(perm)-1, 0, -1):
        curr += costs[perm[i]][perm[i-1]]
    curr += costs[perm[0]][perm[-1]]
    max_happiness = max(max_happiness, curr)

print(max_happiness)

# similar to the traveling salesman problem; imagine a fully connected graph,
# you would have to find the max cost to traverse all of them with the cost
# iin between vertexes the increase/decrease in happiness
