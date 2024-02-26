import random 

def play():
    choices = ['r', 'p', 's']
    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n").lower()

    while user not in choices:
        print("Invalid choice. Please choose 'r' for rock, 'p' for paper, or 's' for scissors.")
        user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n").lower()

    computer = random.choice(choices)

    if user == computer:
        return "It's a tie"
    
    elif is_win(user, computer):
        return "Congratulations! You won!"
    
    else:
        return 'Sorry, You lost!!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's' ) or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r' ):
        return True
    else:
        return False
         
print(play())
