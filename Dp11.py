var1 = []
prime_array = []
for all1 in range(0, 1000, 100):
    a = all1 + 100
    prime_array.append(a)
    for some in range(all1+1, a+1):
        for i in range(2, some):
            if (some % i) == 0:
                break
        else:  
            prime_array.append(some)
            
    var1.append(prime_array)
    prime_array = []

for row in var1:
    for elem in row:
        print(elem, end=' ')
    print()

