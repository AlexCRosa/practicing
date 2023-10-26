def main():

    choices = ["rock", "scissors", "paper"]

    def player1():
        while True:
            try:
                choice = input("Player 1, what's your choice? ").lower()
                if choice in choices:
                    player = choice
                    return player
            except ValueError:
                print("Not a valid choice.")

    def player2():    
        while True:
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
        while True:    
            possible_answers = ["yes", "no"]


    while True:
        player1()
        player2()
        game_logic(player1, player2)
        
        check = input("Do you want to play again? ").lower()
        if check in ["yes", "no"] and check == "yes":
            continue
        else:
            break
 
main()