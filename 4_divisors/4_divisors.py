# Prompt the user for a number
num = int(input("Tell me a number: "))

x = range(0, num)

# Create a list of all divisors of the given number
new_list = []

# Check the divisors
for i in x:
    if i % 