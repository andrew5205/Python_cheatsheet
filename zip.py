# The zip() function returns a zip object, 
# which is an iterator of tuples where the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

zipped = zip(numbers, letters)
print(zipped)                   # [(1, 'a'), (2, 'b'), (3, 'c')]
print(type(zipped))             # <type 'list'>

print(list(zipped))             # [(1, 'a'), (2, 'b'), (3, 'c')]



# return type is list, NOT dictionary
s1 = [2, 3, 1]
s2 = ['b', 'a', 'c']

unorderZipped = zip(s1, s2)
print(unorderZipped)            # [(2, 'b'), (3, 'a'), (1, 'c')]

# for k, v in unorderZipped.items():      # AttributeError: 'list' object has no attribute 'items'
#     print(k)
#     print(v)


# zip(*list) 
# * in a function called "unpacks" 
# like split() for JS 


# each str in the list is also a list 
# use * to split into alphabet 

strs = ["flower","flow","flight"]
for i in zip(*strs):
    print(i)
    print(set(i))

# ('f', 'f', 'f')
# ('l', 'l', 'l')
# ('o', 'o', 'i')
# ('w', 'w', 'g')



# set() method is used to convert any of the iterable to sequence of iterable elements 
# with dintinct elements, commonly called Set.

# set(i)

# set(['f'])
# set(['l'])
# set(['i', 'o'])
# set(['g', 'w'])
