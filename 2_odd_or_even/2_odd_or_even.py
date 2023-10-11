num = int(input("Tell me a number: "))
check = int(input("Tell me a number to divide by: "))

if num % 4 == 0:
    print("This number is a multiple of 4.")

elif num % 2 == 0:
    print("The number given is even!")

else:
    print("The number given is odd!")


if num % check == 0:
    print(f"{num} divides evenly by {check}.")

elif num % check > 0:
    print(f"{num} modulo {check} is {num % check}.")