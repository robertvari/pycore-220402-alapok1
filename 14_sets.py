numbers1 = {1, 2, 3, 4}
numbers2 = {3, 4, 5, 6}

# combine two sets
print(numbers1 | numbers2)

# remove duplicates from a list
name_list = ["kriszta", "csaba", "tamás", "csaba", "kriszta"]
print(list(set(name_list)))

# intersection
print(numbers1 & numbers2)

# difference
print(numbers2 - numbers1)

# symmetrical difference
print(numbers1 ^ numbers2)

# add item to a set
numbers1.add(5)
print(numbers1)

# add multiple items to a set
numbers1.update([6, 7, 8, 9])
print(numbers1)

# remove item from a set
numbers1.discard(8)
print(numbers1)

# throws an error if item not in set
numbers1.remove(9)
print(numbers1)

# set operators with strings
# print(set("abcde") & set("defg"))