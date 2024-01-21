# File Name:       day_09/part_2.py
# Author:          Samuel Wang (@samuelpswang)
# Purpose:         AoC 2015 Day 9 Part 2 (https://adventofcode.com/2015/day/9)
# Last Updated:    21 Jan 2023

from itertools import permutations

costs = {}
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        deststr, coststr = line.split(" = ")
        dest1, dest2 = deststr.split(" to ")
        if dest1 not in costs:
            costs[dest1] = {}
        if dest2 not in costs:
            costs[dest2] = {}
        costs[dest1][dest2] = int(coststr)
        costs[dest2][dest1] = int(coststr)

dests = []
for dest in costs:
    dests.append(dest)

perms = permutations(dests)
max_cost = 0
for perm in perms:
    curr = 0
    for i in range(len(perm)-1):
        curr += costs[perm[i]][perm[i+1]]
    max_cost = max(max_cost, curr)

print(max_cost)

# this is equivalent ot the traveling salesman problem
# brute force checking is effective for small number of nodes
