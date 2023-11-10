import random

generate_number = random.randint(1, 10)
attempts = 0

while True:
    user_input = input("Guess a number between 1 and 10? ")

    if user_input.lower() == "exit":
        print(f"You made {attempts} attempts.")
        print("See you later!")
        break

    try:
        user_guess = int(user_input)
        attempts += 1            

        if user_guess > generate_number:
            print("That's HIGH! Guess another number: ")
        elif user_guess < generate_number:
            print("That's LOW! Guess another number: ")
        else:
            print(f"Well done! The number is {generate_number}. :)")
            print("Let's keep playing! To stop, type 'exit'.")
            generate_number = random.randint(1, 10)
            attempts += 1
    except ValueError:
        print("Please enter a valid number or type 'exit'.")