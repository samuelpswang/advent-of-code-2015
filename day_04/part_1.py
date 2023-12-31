from hashlib import md5

def is_valid(key, num):
    hexhash = md5((key+str(num)).encode()).hexdigest()
    return all(hexhash[i] == '0' for i in range(5))

key = ""
with open("input.txt", "r") as file:
    key = file.readline()

num = 0
while not is_valid(key, num): 
    num += 1

print(num)
