from random import randint
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
chosen_num = randint(1, 100)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def game():
    count = set_difficulty()
    user_input = ""
    while user_input != chosen_num and count != 0:
        print(f"You have {count} attempts remaining to guess the number.")
        user_input = int(input("Make a guess: "))
        if user_input == chosen_num:
            print(f"You got it! The answer was {chosen_num}")
        elif count != 0 and user_input > chosen_num:
            print("Too high.")
            print("Guess again.")
        elif count != 0  and user_input < chosen_num:
            print("Too low.")
            print("Guess again.")
        count -= 1
        if count == 0:
            print("You've run out of guesses, you lose")
def set_difficulty():
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
game()

