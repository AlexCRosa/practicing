def main():

    choices = ["rock", "scissors", "paper"]

    def player1(status):
        while status:
            try:
                choice = input("Player 1, what's your choice? ").lower()
                if choice in choices:
                    player1 = choice
                    return player1
            except ValueError:
                print("Not a valid choice.")

    def player2(status):    
        while status:
            try:
                choice = input("Player 2, what's your choice? ").lower()
                if choice in choices:
                    player2 = choice
                    return player2
            except ValueError:
                print("Not a valid choice.")            

    def game_logic(player1, player2):
        if player1 == player2:
            print("Drawn.")
        elif player1 == "rock" and player2 == "scissors":
            print("Player 1 wins!")
        elif player1 == "rock" and player2 == "paper":
            print("Player 2 wins!")
        elif player1 == "scissors" and player2 == "rock":
            print("Player 2 wins!")
        elif player1 == "scissors" and player2 == "paper":
            print("Player 1 wins!")
        elif player1 == "paper" and player2 == "rock":
            print("Player 1 wins!")
        elif player1 == "paper" and player2 == "scissors":
            print("Player 2 wins!")

    def check_new_game():
        possible_answers = ["yes", "no"]
        check = input("Play again? ").lower()
        if check in possible_answers and check == "no":
            status = False
            return status
        elif check in possible_answers and check == "yes":
            status = True
            return status
        elif check not in possible_answers:
            print("Invalid choice. Type 'yes' or 'no'.")

    status = True

    player1 = player1(status)
    player2 = player2(status)

    game_logic(player1, player2)

    check_new_game()
 
main()