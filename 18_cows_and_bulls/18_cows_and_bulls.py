import random

print("Welcome to the Cows and Bulls Game!")
# Create and store a random number into a list
random_number = random.randint(1000, 9999)
generated_number = [int(i) for i in str(random_number)]

# Keep track of the number of user guesses
guesses = 0

# Managing user's guess inside a while loop
while True:
    # Ask user for guess a number
    guessed_number = int(input("Enter a number: "))

    # Store user's guess into a list
    guessed_number = [int(i) for i in str(guessed_number)]

    # Comparing user guessing number and generated number
    if generated_number == guessed_number:
        guesses += 1
        print(f"Well done! You have done {guesses} attempts.")
        break
    else:
        guesses += 1
        # Compare the generated number and user's guess
        cows = 0
        bulls = 4
        if generated_number[0] == guessed_number[0]:
            cows += 1
            bulls -= 1
        if generated_number[1] == guessed_number[1]:
            cows += 1
            bulls -= 1
        if generated_number[2] == guessed_number[2]:
            cows += 1
            bulls -= 1
        if generated_number[3] == guessed_number[3]:
            cows += 1
            bulls -= 1

        # Print a message based on the result
        print(f"{cows} cows, {bulls} bulls")