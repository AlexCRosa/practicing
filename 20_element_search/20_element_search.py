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
    
def binary_search(ordered_list, given_number):
    start = 0
    end = len(ordered_list) - 1

    while start <= end:
        # Find the middle element in the list
        mid = (start + end) // 2
        middle_element = ordered_list[mid]

        # Check if the middle element is the given number
        if middle_element == given_number:
            print(f"{given_number} is on the list.")
            return True
        
        # if middle element is less than the given number
        elif middle_element < given_number:
            # Sum 1 to the middle element position
            start = mid + 1
        else:
            # Decrease 1 to the middle element position
            end = mid - 1

    print(f"{given_number} is not in the list.")
    return False

given_number = random.randint(1, 100)
ordered_list = list_creator()


# Printing the list to help identify if the output is ok
print(ordered_list)
print(given_number)

# Simple method to check if given number is on the list
print(check_element(ordered_list, given_number))

# Using binary search to check if the given number is on the list
binary_search(ordered_list, given_number)