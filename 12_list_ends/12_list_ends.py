a = [5, 10, 15, 20, 25]

def rewriting_list(list):
    new_list = []
    
    # Get elements
    new_list.append(list[-1])
    new_list.append(list[0])

    # Sort elements
    new_list.sort()
    
    return new_list

print(rewriting_list(a))