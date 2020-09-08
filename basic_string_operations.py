

astring = "HelloWorld!"

print(len(astring))             # 11
print(astring.index("o"))       # 4
print(astring.count("l"))       # 3
print(astring[3:7])             # loWo

# [start:stop:step]
print(astring[3:7:2])           # lw
print(astring[3:7:1])           # loWo


print(astring[::1])             # HelloWorld!
print(astring[::-1])            # !dlroWolleH


print(astring.upper())          # HELLOWORLD!
print(astring.lower())          # helloworld!



print(astring.startswith("Hello"))      # True
print(astring.endswith("asdasd"))       # False


bstring = " hello world !"
print(bstring.split(" "))       # ['', 'hello', 'world', '!']
print(astring.split(" "))       # ['HelloWorld!']
