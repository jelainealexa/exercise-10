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

# Create new list based on condition
result_list = new_list(list_1, list_2)

# 