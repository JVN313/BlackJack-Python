from classes import*

p_name = input("Enter Player Name: ")
player1 = Player(p_name)
dealer = Player("The Dealer")
dealer_win_range = [18, 19, 20]

def Replay(player_input):
    global player1, dealer
    if player_input == "y":
        player1 = Player(p_name)
        dealer = Player("The Dealer")
        GameLoop()
    else:
        print(f"Thanks For Playing {p_name}")
        quit()

def GameLoop():
    #Player Game Logic
    while player1.hand.total < 21:
        
        choice = input(f"Your Hand Amount is {player1.hand.total}. Would You Like To Hit Or Stay?: ").upper()

        if choice == "H":
            player1.hand.Hit()
            print(player1.hand.total)
        elif choice == "S":
            print(f"It's {dealer.name}'s Turn")
            break

        if player1.hand.total > 21:
            print("You Lose!")
            Replay(input("Would You Like To Play Again? "))
        elif player1.hand.total == 21:
            print(f"{player1.name} You Won!")
            Replay(input("Would You Like To Play Again? "))

    if dealer.hand.total == 21:
            print(f"Sorry {player1.name} {dealer.name} Won The Game")
            Replay(input("Would You Like To Play Again? "))

    #The Dealer Game Logic
    while dealer.hand.total < 21:

        print(f"{dealer.name}'s Hand Is {dealer.hand.total}")
        print(f"{dealer.name} Hits")
        dealer.hand.Hit()

        if dealer.hand.total in dealer_win_range:
            print(f"{dealer.name} Stays With {dealer.hand.total}")
            break

        if dealer.hand.total == 21:
            print(f"{dealer.name} Hit 21")
            print(f"Sorry {player1.name} {dealer.name} Won The Game")
            Replay(input("Would You Like To Play Again? "))
        elif dealer.hand.total > 21:
            
            print(f"{dealer.name} Bust! You Win!")
            Replay(input("Would You Like To Play Again? "))
        
    if player1.hand.total > dealer.hand.total:
        print(f"{player1.name} You Won!")
        Replay(input("Would You Like To Play Again? "))
    elif player1.hand.total < dealer.hand.total:
        print(f"Sorry {player1.name} {dealer.name} Won The Game")
        Replay(input("Would You Like To Play Again? "))
    else:
        print("Draw!")
        Replay(input("Would You Like To Play Again? "))


if player1.hand.total == 21:
    print(f"{player1.name} You Won!")
    Replay(input("Would You Like To Play Again? "))

GameLoop()