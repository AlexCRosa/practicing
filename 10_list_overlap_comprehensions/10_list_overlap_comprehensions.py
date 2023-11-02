import random

list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(set(list_a).intersection(set(list_b))))

# Traditional way

# new_list = []

# for i in list_a:
#     if (i in list_b) and (i not in new_list):
#         new_list.append(i)

# print(new_list)

def generate_random_list(length, min_value, max_value):
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list

random_list_a = generate_random_list(15, 1, 25)
random_list_b = generate_random_list(10, 1, 25)

print(list(set(random_list_a).intersection(set(random_list_b))))