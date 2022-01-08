import random
class Card():

    def __init__(self):
        self.value = random.randint(2,11)

class Hand():

    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.total = card1.value + card2.value

    def Hit(self):
        new_card = Card()
        self.total += new_card.value

class Player():

    def __init__(self):
        self.name = input("Enter Player name: ")
        self.hand = Hand(Card(), Card())

player1 = Player()

if player1.hand.total == 21:
    print(f"{player1.name} You Won!")
    quit()


choice = input(f"Your Hand Amount is {player1.hand.total}. Would You Like?: ").upper()

if choice == "H":
    player1.hand.Hit()
    print(player1.hand.total)

