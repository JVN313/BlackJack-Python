from classes import*

player1 = Player()

if player1.hand.total == 21:
    print(f"{player1.name} You Won!")
    quit()


choice = input(f"Your Hand Amount is {player1.hand.total}. Would You Like?: ").upper()

if choice == "H":
    player1.hand.Hit()
    print(player1.hand.total)
