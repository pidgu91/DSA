def find_second_smallest(my_list):
    sorted_list = sorted(my_list)
    if len(sorted_list) < 2:
        return None
    else:
        return sorted_list[1]

def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    
    for number in my_list:
        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest:
            second_smallest = number
    return second_smallest



print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest_v2([5, 8, 3, 2, 6]))

