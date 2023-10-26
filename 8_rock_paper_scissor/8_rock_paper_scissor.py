def main():

# Get players choice
    def get_player_choice():
        while True:
                choice = input("What's your choice (rock, paper, or scissors)? ").lower()
                if choice in ["rock", "scissors", "paper"]:
                    return choice
                else:
                    print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")           

# Create the game logic
    def game_logic(player1, player2):
        if player1 == player2:
            return "It's a tie!"
        elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
            return "Player 1 wins!"
        elif (player1 == "rock" and player2 == "paper") or (player1 == "scissors" and player2 == "rock") or (player1 == "paper" and player2 == "scissors"):
            return "Player 2 wins!"

# Ask user to decide wether play a new game or not
    def check_new_game():
        while True:
            check = input("Do you want to play again? ").lower()
            if check in ["yes", "no"]:
                if check == "yes":
                    return check
                elif check == "no":
                    return check
            else:
                print("Invalid answer. Do you want to play again? Answer 'yes' or 'no'.")

# Since the user may choose to play the game more then once, the program must run on a loop
    while True:
        player1_choice = get_player_choice()
        player2_choice = get_player_choice()

        print(f"Player 1 chose {player1_choice}.")
        print(f"Player 2 chose {player2_choice}.")

        winner = game_logic(player1_choice, player2_choice)
        print(winner)

        new_game = check_new_game()
        if new_game == "yes":
            print("Ok. Lets go!")
            continue
        elif new_game == "no":
            print("Thank you!")
            break     
 
main()