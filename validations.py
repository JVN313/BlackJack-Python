def Choice_Validation(choice):
    choice_options = ["H","HIT","STAY","S"]
    while choice not in choice_options:
        print("Invalid Response! Please Enter 'HIT' or 'STAY'")
        choice = input("Would You Like To Hit Or Stay?: ").upper()
    
    return choice

def Replay_Validation(player_input):
    PI_options = ["Y","YES","N","NO"]
    while player_input not in PI_options:
        print("Invalid Response! Please Enter 'YES' or 'NO'")
        player_input = input("Would You Like To Play Again? ").upper()
    
    return player_input
    