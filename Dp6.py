hash_fun = {}
ip = [45,44,55,77,26,93,17,31,20,54]

for i in ip:
    key = i%11
    if key in hash_fun:
        hash_fun[key].append(i)
    else:
        hash_fun[key] = [i]

print("Hash function = ",hash_fun)

number = int(input("Enter which Number you want to search? = "))
key = number%11
if key in hash_fun:
    values = hash_fun.get(key)
    if number in values:
        print("Number found...")
    else:
        print("No such number available...")
else:
    print("Not found")
