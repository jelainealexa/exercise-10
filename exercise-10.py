# Create a new list from two list using the following condition
def new_list(list_1, list_2):
    # Empty list
    result_list = []

    # Iterate first list
    for i in list_1:
        if i % 2 != 0:
            result_list.append(i)

    # Iterate second list
    for i in list_2:
        if i % 2 == 0:
            result_list.append(i)
    
    return result_list

# Given
list_1 = [23, 45, 86, 90, 13, 14]
list_2 = [18, 76, 77, 95, 24, 45]

result_list = new_list(list_1, list_2)

# Print new list
print(f"Result is: ", result_list)