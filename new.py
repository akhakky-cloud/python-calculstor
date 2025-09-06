# 1. Create an empty list
my_list = []

# 2. Append numbers 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. Append 50
my_list.append(50)

# 4. Remove the first element (10)
my_list.pop(0)

# 5. Extend with [60, 70]
my_list.extend([60, 70])

# 6. Print all items
print("Current items in my_list:", my_list)

# 7. Find and print index of 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)