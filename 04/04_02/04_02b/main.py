# order doesn't matter for sets
# usually testing to see if it is a part of the set
# with sets, key is the value
# we almost never use sets for retrieval of data

primary_colors = {"red", "blue", "yellow"}
color = "green"

if color in primary_colors:
  print(color + " is a primary color")
else:
  print(color + " is not a primary color")

letters = set(['a', 'b'])
letters.add('c')
print(letters)
