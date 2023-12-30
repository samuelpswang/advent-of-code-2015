def count_chr(src, tar):
    count = 0
    for ch in src:
        if ch == tar:
            count += 1
    return count
        
def count_literal_encode(literal):
    return len(literal) + count_chr(literal, "\\") + count_chr(literal, "\"") + 2

total = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip('\n')
        rep = len(line)
        enc = count_literal_encode(line)
        total += enc-rep

print(total)
