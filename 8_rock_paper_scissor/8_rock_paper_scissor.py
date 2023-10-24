def main():

    choices = ["rock", "scissors", "paper"]

    def player1():
        while True:
            try:
                choice = input("Player 1, what's your choice? ")
                if choice in choices:
                    player1 = choice
            except ValueError:
                print("Not a valid choice.")
            else:
                return player1

    def player2():    
        while True:
            try:
                choice = input("Player 2, what's your choice? ")
                if choice in choices:
                    player2 = choice
            except ValueError:
                print("Not a valid choice.")
            else: 
                return player2
            

    player1 = player1()
    player2 = player2()

main()