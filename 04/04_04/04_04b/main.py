primary_colors = frozenset(["red", "blue", "yellow"])

if "blue" in primary_colors:
  print("Blue is in the set")

# Frozen sets are immutable
# Provides unwanted changes to a set
primary_colors.add("green")

