class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()                # This is a message inside the class.
print(myobjectx.variable)           # blah


myObjecty = MyClass()
myObjecty.variable = "Object revised"
print(myObjecty.variable)           # Object revised