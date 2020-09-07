

name = "Doe"
print("my name is John %s !" %name)


age = 23
print("my name is %s, and I am %d years old" %(name, age))



data = ["Jonh", "Doe", 23]

format_string = "Hello {} {}. Your are now {} years old"
print(format_string.format(data[0], data[1], data[2]))


# tuple is a collection of objects which ordered and immutable
format_string2 = "Hello %s %s, you are %s years old"
print(format_string2 % tuple(data))




# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)
