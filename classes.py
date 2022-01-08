import random
class Card():

    def __init__(self):
        self.value = random.randint(1,11)

class Hand():

    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.total = card1.value + card2.value

    def Hit(self):
        new_card = Card()
        self.total += new_card.value

class Player():

    def __init__(self, name):
        self.name = name
        self.hand = Hand(Card(), Card())
