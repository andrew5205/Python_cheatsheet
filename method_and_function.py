
# Method is called by its name, but it is associated to an object (dependent).
# A method is implicitly passed the object on which it is invoked.
# It may or may not return any data.
# A method can operate on the data (instance variables) that is contained by the corresponding class


# Python 3  User-Defined  Method 
class ABC : 
    def method_abc (self): 
        print("I am in method_abc of ABC class. ") 

class_ref = ABC() # object of ABC class 
class_ref.method_abc()                  # I am in method_abc of ABC class. 




import math 

ceil_val = math.ceil(15.25) 
print("Ceiling value of 15.25 is : ", ceil_val)     # ('Ceiling value of 15.25 is : ', 16.0)
print("Ceiling value of 15.25 is : "), ceil_val     # Ceiling value of 15.25 is :  16.0


# The sum() function adds the items of an iterable and returns the sum.
    # iterable - iterable (list, tuple, dict, etc). The items of the iterable should be numbers.
    # start (optional) - this value is added to the sum of items of the iterable. The default value of start is 0 (if omitted)

s = sum([5, 15, 2]) 
print( s ) # prints 22 

sum_s = sum([s, 10])
print(sum_s)    # prints 32 

mx = max(15, 6) 
print( mx ) # prints 15 


# order is not guaranteed for set collection
test = {'a', 'P', 'p', 'l', 'e'}
separator = '-->'
print(separator.join(test))        # a-->P-->e-->l-->p