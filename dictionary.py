
dict = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3'
}

print(dict['key1'])         # value1


# print(dict[key1])         # NameError
# print(dict[value1])       # NameError

# order not guaranteed
for i in dict:
    print(dict[i])       # value3
                        # value2
                        # value1


dictA = {
    "1" : "first val",
    "2" : "second val",
    "3" : "third val"
}
dictA.pop("2")
print(dictA)             # {'1': 'first val', '3': 'third val'}

# assign key : val  directly 
dictA["4"] = "fourth val"
print(dictA)            # {'1': 'first val', '3': 'third val', '4': 'fourth val'}


# update
dictA.update({"5" : "fifth val", "6" : "six val"})
print(dictA)            # {'1': 'first val', '3': 'third val', '5': 'fifth val', '4': 'fourth val', '6': 'six val'}

if "6" in dictA:
    print("got it")         # got it
    print(dictA["6"])       # six val



print("dict['key2']: ", dict["key2"])        # dict['key2']:  value2
