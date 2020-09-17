
# python sorted is straight forward 
# The sorted() function returns a sorted list of the specified iterable object.

# sort tuple

tuple = ("b", "g", "a", "d", "f", "c", "h", "e")
t = sorted(tuple)
print(t)                # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


# numeric
nums = (1,2,3,9,5,6,4,7,8)
num = sorted(nums)
print(num)              # [1, 2, 3, 4, 5, 6, 7, 8, 9]



a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse = True)             # ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
print(x)
y = sorted(a, reverse = False)          # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(y)
