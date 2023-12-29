import hashlib

key = open("input.txt").read().removesuffix("\n")

to_add = 0
while True:
    new_key = key+str(to_add)
    result = hashlib.md5(new_key.encode())
    if result.hexdigest()[:6] == "000000":
        break
    to_add += 1

print(to_add)
