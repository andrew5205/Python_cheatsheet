
primes = [2, 3, 5, 7]
for p in primes:
    print(p)        # 2
                    # 3 
                    # 5
                    # 7



for x in range(5):
    print(x)        # 0, 1, 2, 3, 4 

for y in xrange(5):
    print(y)


for z in range(3, 8):
    print(z)                # 3, 4, 5, 6, 7

for v in range(3, 11, 2):
    print(v)                # 3, 5, 7 ,9 


count = 0
while True:
    print(count)
    count +=1
    if count > 5:
        break


# continue is used to skip current block
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
