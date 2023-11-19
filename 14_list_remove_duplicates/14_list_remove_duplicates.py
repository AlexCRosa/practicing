import random

# Prepare two list to store elements
first_list = []
second_list = []

# Function to create a list of random numbers
def create_list():
    counter = 0

    while counter < 20:
        first_list.append(random.randint(1, 30))
        counter += 1

# Function to exclude the duplicate elements
def exclude_duplicate():
    for i in first_list:
        if i not in second_list:
            second_list.append(i)
        else:
            continue

create_list()
first_list.sort()
print(first_list)

# Since sets ignore duplicates, I do not need to manage first_list elements
print(set(first_list))

exclude_duplicate()
print(second_list)

# print(list(set(a).intersection(set(b))))