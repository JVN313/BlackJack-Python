from classes import*
from validations import*

p_name = input("Enter Player Name: ")
player1 = Player(p_name)
dealer = Player("The Dealer")
dealer_win_range = [18, 19, 20]

def Replay():
    global player1, dealer
    player_input = input("Would You Like To Play Again? \n").upper()
    if Replay_Validation(player_input) == "Y" or Replay_Validation(player_input) == "YES":
        player1 = Player(p_name)
        dealer = Player("The Dealer")
        GameLoop()
    elif Replay_Validation(player_input) == "N" or Replay_Validation(player_input) == "NO":
        print(f"Thanks For Playing {p_name}")
        quit()

def GameLoop():
    #Player Game Logic
    while player1.hand.total < 21:
        
        print(f"Your Hand Amount is {player1.hand.total}.")
        choice = Choice_Validation( input("Would You Like To Hit Or Stay?: \n").upper())

        if choice == "H" or choice == "HIT":
            player1.hand.Hit()
            print(f"{player1.hand.total}\n")
        elif choice == "S" or choice == "STAY":
            print(f"It's {dealer.name}'s Turn\n")
            break

        if player1.hand.total > 21:
            print("You Lose!")
            Replay()
        elif player1.hand.total == 21:
            print(f"{player1.name} You Won!")
            Replay()

    if dealer.hand.total == 21:
            print(f"Sorry {player1.name} {dealer.name} Won The Game")
            Replay()

    #The Dealer Game Logic
    while dealer.hand.total < 21:

        print(f"{dealer.name}'s Hand Is {dealer.hand.total}")
        print(f"{dealer.name} Hits\n")
        dealer.hand.Hit()

        if dealer.hand.total in dealer_win_range:
            print(f"{dealer.name} Stays With {dealer.hand.total}")
            break

        if dealer.hand.total == 21:
            print(f"{dealer.name} Hit 21")
            print(f"Sorry {player1.name} {dealer.name} Won The Game")
            Replay()
        elif dealer.hand.total > 21:
            
            print(f"{dealer.name} Bust! You Win!")
            Replay()
        
    if player1.hand.total > dealer.hand.total:
        print(f"{player1.name} You Won!")
        Replay()
    elif player1.hand.total < dealer.hand.total:
        print(f"Sorry {player1.name} {dealer.name} Won The Game")
        Replay()
    else:
        print("Draw!")
        Replay()


if player1.hand.total == 21:
    print(f"{player1.name} You Drew 21! You Won!")
    Replay()

GameLoop()