from functools import reduce

iterations = 50

prompt = ""
with open("input.txt", "r") as file:
    for line in file:
        prompt = line.strip("\n")
        
def looksay(prompt):
    count = -1
    prev = -1
    next_prompt = ""
    for ch in prompt:
        if prev == -1:
            prev = int(ch)
            count = 1
        elif prev == int(ch):
            count += 1
        else:
            next_prompt += str(count) + str(prev)
            prev = int(ch)
            count = 1
    next_prompt += str(count) + str(prev)
    return next_prompt

prompt = reduce(lambda prev, i: looksay(prev), range(iterations), prompt)
print(len(prompt))

# brute force takes around 13 mins to complete on M1 Pro
# as pointed out by John Conway himself, the length grows in exponential terms
# using reduce or recursion is much better, as inspired by @mjpieters
# also note the possible use of the "groupby" function in the itertools library
