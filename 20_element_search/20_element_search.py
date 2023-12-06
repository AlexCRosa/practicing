import random

# I created this function just to creating a list as requested
def list_creator():
    amount_elements = 20
    new_list = []
    while len(new_list) < amount_elements:
        new_element = random.randint(1, 50)

        # Avoiding duplicates
        if new_element not in new_list:
            new_list.append(new_element)
            
    new_list.sort()
    return new_list

def check_element(ordered_list, given_number):
    # Check if the user's number is in the list
    if given_number in ordered_list:
        return True
    else:
        return False
    
given_number = random.randint(1, 100)
ordered_list = list_creator()


# Printing the list to help identify if the output is ok
print(ordered_list)
print(given_number)

print(check_element(ordered_list, given_number))