import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Create a new list to receive the data
new_list = []

# Iterate through list a
for i in a:

# Check if the number is present in both lists + exclude duplicates
    if i in b and i not in new_list:
        new_list.append(i)

print(new_list)

# Extra 1: Program to create random lists
def generate_random_list(length, min_value, max_value):
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list

# Creating the random lists
list_1 = generate_random_list(15, 1, 25)
list_2 = generate_random_list(10, 1, 25)

extra_list = []

# Iterate through lists created
for i in list_1:

# Check if the number is present in both lists + exclude duplicates
    if i in list_2 and i not in extra_list:
        extra_list.append(i)

print(sorted(extra_list))

# Extra 2: Print in one line of Python
# Exercise 14 asked me to move below code inside a function
def using_set():
    print(list(set(a).intersection(set(b))))

using_set()