set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

# Joining each set
union_set = set_A.union(set_B)
print(union_set)

# Items that are in both sets
intersection_set = set_A.intersection(set_B)
print(intersection_set)

# Items that are not in set B - 10,20
difference_set = set_A.difference(set_B)
print(difference_set)

# Items that are not in set A - 60, 70
difference_set_BA = set_B.difference(set_A)
print(difference_set_BA)

# All the items that they don't share
symmetric_difference = set_A.symmetric_difference(set_B)
print(symmetric_difference)

