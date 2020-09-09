

name = "John"
if name in ["John", "Mike"]:
    print("name in pool")


mylist = ["1", "2", "3", "4", "5", 6]
myInput = "5"
if myInput in mylist:
    print("found it")       # found it

myInput2 = 6
if myInput2 in mylist:      # got it
    print("got it")


# Tenrary Operator 
# [value_if_true] if condition else [value_if_false]
[a , b, c, d] = [10, 20, 100, 50] 
t = a if a < b else b
print(t)

f = c if c < d else d
print(f)



print(not True)         # False
print(not False)        # True



# is operator 
# The is keyword is used to test if two variables refer to the same object.

x = ["apple", 'banana', "orange"]
y = x 
print( x == y)          # True


w = ["tree", "flower", "grass"]
v = ["tree", "flower", "grass"]
print( w is v)          # False