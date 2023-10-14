# Prompt the user for a number
num = int(input("Tell me a number: "))

# Create a list of all divisors of the given number
new_list = []

# Loop through numbers from 1 to the given number
for i in range(1, num + 1):

    # Check the divisors
    if num % i == 0:
        new_list.append(i) 

print(new_list)