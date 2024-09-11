# Linear Search
my_list = [8, 5, 0, 3, 9, 7]
ITEM = 7

def search(item, list):
  for element in list:
    if element == item:
      return True
  return False

print(search(ITEM, my_list))


# Brute force method
# Simple, but very slow if you have a lot of items

ITEM_INDEX = my_list.index(ITEM)



