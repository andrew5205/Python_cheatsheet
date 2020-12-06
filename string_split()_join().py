
# split()

string = " a part of all you earn is yours to keep"
# s = string.split()

print(string.split())               # ['a', 'part', 'of', 'all', 'you', 'earn', 'is', 'yours', 'to', 'keep']

print(string.split(" "))            # ['', 'a', 'part', 'of', 'all', 'you', 'earn', 'is', 'yours', 'to', 'keep']

print(string.split("a"))            # [' ', ' p', 'rt of ', 'll you e', 'rn is yours to keep']


another_string = " a part, of all you earn, is yours to keep"

print(another_string.split())           # ['a', 'part,', 'of', 'all', 'you', 'earn,', 'is', 'yours', 'to', 'keep']
print(another_string.split(","))        # [' a part', ' of all you earn', ' is yours to keep']




# join()
# x.join(y) - x: seprator, y: attribute 

string = "abcde"
print(",".join(string))         # a,b,c,d,e
print("".join(string))          # abcde
print(" ".join(string))         # a b c d e



