def has_unique_characters(data):
    new_set = set(data)
    print(new_set)
    return len(new_set) == len(data)


print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))

# need to get the character and check to see if its in the set, if not get the next letter
# 

