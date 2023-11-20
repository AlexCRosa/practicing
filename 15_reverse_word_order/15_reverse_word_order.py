first_string = "My name is Michele"

# Receiving and managing data
def managing_data():
    new_list = first_string.split()
    new_list.reverse()

# Creating a new list with the elements in the reverse order
    new_string = []
    for i in new_list:
        new_string.append(i)
    
    return new_string

# Printing the new string
def printing_string():
    for i in new_string:
        print(i, end=" ")

new_string = managing_data()
printing_string()