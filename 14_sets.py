numbers1 = {1, 2, 3, 4}
numbers2 = {3, 4, 5, 6}

# combine two sets
print(numbers1 | numbers2)

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

# set operators with strings
# print(set("abcde") & set("defg"))