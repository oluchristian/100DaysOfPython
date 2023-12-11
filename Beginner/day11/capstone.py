import random
from art import logo

def initialize_game():
    global cards, list_user_card, computer_cards
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    list_user_card = []
    computer_cards = []

def user_card(cards):
    rand = random.choice(cards)
    list_user_card.append(rand)
    return rand

def rand_comp_card(cards):
    rand = random.choice(cards)
    computer_cards.append(rand)
    return rand
print(logo)
def blackjack():
        initialize_game()
        print(f"Your cards: [{user_card(cards)}, {user_card(cards)}], current score: {sum(list_user_card)}")
        print(list_user_card)
        print(f"Computer's first card: {rand_comp_card(cards)}")
        rand_comp_card(cards)
        stay_loop = True
        while sum(list_user_card) < 21 and sum(computer_cards) < 21 and stay_loop:
            get_card = input("Type 'y' to get another card, type 'n' to pass:" )
            if get_card == 'y':
                user_card(cards)
                print(f"Your cards: {list_user_card}, current score: {sum(list_user_card)}")
                print(f"Computer's first card: {computer_cards[0]}")
            elif get_card == 'n':
                while sum(computer_cards) <= 16:
                    rand_comp_card(cards)
                    # computer_cards.append(pass_card)
                stay_loop = False
        max_value = max(sum(computer_cards), sum(list_user_card))
        print(f"Your final hand: {list_user_card}, fianl score: {sum(list_user_card)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        if sum(computer_cards) > 21:
            print("Opponent went over. You win 😁")
        elif sum(list_user_card) > 21:
            print("You went over. You lose 😤")
        elif sum(computer_cards) == 21:
            print("Lose, opponent has Blackjack 😱")
        elif sum(list_user_card) == 21:
            print("Win, you have a Blackjack 😱")
        elif sum(computer_cards) == sum(list_user_card):
            print("Draw 🙃")
        elif max_value > 16:
            if max_value == sum(list_user_card):
                print("You win 😁")
            else:
                print("You lose 😤")
            

start = input("Do you want to play a game of black jack? ")
if start == 'y':
    blackjack()
    play_again = input("Do you want to play again? y/n ")
    while play_again == 'y':
        blackjack()
        play_again = input("Do you want to play again? y/n ")
    print("Goodbye")
else:
    print("Goodbye")