import random
def guess(x):
    res = random.randint(1, x)
    guess = 0
    while guess!=res:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < res:
            print('Sorry, your guess is too Low.')
        elif guess >res:
            print('Sorry, your guess is too high.')
    print(f"Congrats. You have guessed the number {res} correctly!")

print(guess(78))
