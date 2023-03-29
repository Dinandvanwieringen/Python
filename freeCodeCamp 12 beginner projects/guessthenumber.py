import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Higher')
        elif guess > random_number:
            print('Lower')
    
    print(f'You guessed {random_number}. How did you know?')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'correct':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} high, low or correct? ')
        if feedback == 'high':
            high = guess - 1
        elif feedback == 'low':
            low = guess + 1

    print(f'AI TOO STRONG, they knew that youre number was {guess}')

# met computer guess speel je de versie waar de computer jou getal moet raden
# met guess moet je de computers getal raden
computer_guess(10)