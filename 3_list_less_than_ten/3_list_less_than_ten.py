given_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []
    
# Make a new list that has all the elements less than 5
for i in given_list:
    if i < 5:
        new_list.append(i)

# Print out the new list
for i in new_list:
    print(i, end = " ") # Write the numbers in one line

print()

# Ask the user for a number
new_element = int(input("Tell me a number: "))

# Return a list that contains only elements from the original list smaller that the given number
user_list = []

for i in given_list:
    if i < new_element:
        user_list.append(i)

print(user_list)