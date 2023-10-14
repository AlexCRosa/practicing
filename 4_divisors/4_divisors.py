# Prompt the user for a number
num = int(input("Tell me a number: "))

# Create a list of all divisors of the given number
new_list = []

<<<<<<< HEAD
# Loop through numbers from 1 to the given number
for i in range(1, num + 1):

    # Check the divisors
    if num % i == 0:
        new_list.append(i) 
=======
# Check the divisors
for i in x:
    if i % num == 0:
        new_list.append(i)
>>>>>>> 705bbfb20373d383004bb496f861058389dc4fe1

print(new_list)