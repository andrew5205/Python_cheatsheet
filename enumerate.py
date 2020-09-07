
# enumerate


grocery = ['apple', 'orange', 'banana', 'pear', 'melon']
enumerategrocery = enumerate(grocery)

print(type(enumerategrocery))       # <type 'enumerate'>


for item in enumerate(grocery):
    print(item)                     # (0, 'apple')
                                    # (1, 'orange')
                                    # (2, 'banana')
                                    # (3, 'pear')
                                    # (4, 'melon')

print('\n')

for count, item in enumerate(grocery):
    print(count, item)              # (0, 'apple')
                                    # (1, 'orange')
                                    # (2, 'banana')
                                    # (3, 'pear')
                                    # (4, 'melon')


print('\n')

for count, item in enumerate(grocery, 100):
    # change staring value to 100
    print(count, item)              # (100, 'apple')
                                    # (101, 'orange')
                                    # (102, 'banana')
                                    # (103, 'pear')
                                    # (104, 'melon')






