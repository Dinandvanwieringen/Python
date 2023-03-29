import random

def play():
    user = input("Choice: 'rock', 'paper', 'sciccors' ")
    computer = random.choice(['rock', 'paper', 'sciccors'])

    if user == computer:
        return f'Its a tie, the computer also choose {computer}'
    
    if is_win(user, computer):
        return f'You won, the computer choose {computer}'
    
    return f'You lost, the computer choose {computer}'
    
def is_win(player, opponent):
    if (player == 'rock' and opponent == 'sciccors') or (player == 'sciccors' and opponent == 'paper') \
        or (player == 'paper' and opponent == 'rock'):
        return True

print(play())