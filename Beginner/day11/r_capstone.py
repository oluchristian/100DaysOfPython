import random

def blackjack():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    play = True
    list_user_card = []
    def user_card(cards):
        rand = random.choice(cards)
        list_user_card.append(rand)
        return rand

    computer_cards = []
    def rand_comp_card(cards):
        rand = random.choice(cards)
        computer_cards.append(rand)
        return rand
    start = input("Do you want to play a game of black jack? ")
    if start == 'y':
        print(f"Your cards: [{user_card(cards)}, {user_card(cards)}], current score: {sum(list_user_card)}")
        print(list_user_card)
        print(f"Computer's first card: {rand_comp_card(cards)}")
        second_comp_card = rand_comp_card(cards)
        while sum(list_user_card) < 21 and sum(computer_cards) < 21:
            get_card = input("Type 'y' to get another card, type 'n' to pass:" )
            if get_card == 'y':
                new_card = user_card(cards)
                print(f"Your cards: {list_user_card}, current score: {sum(list_user_card)}")
                print(f"Computer's first card: {computer_cards[0]}")
            elif get_card == 'n':
                while sum(computer_cards) <= 16:
                    pass_card = rand_comp_card(cards)
        max_value = max(sum(computer_cards), sum(list_user_card))
        print(f"Your final hand: {list_user_card}, fianl score: {sum(list_user_card)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        if sum(computer_cards) > 21:
            print("Opponent went over. You win 😁")
        elif sum(list_user_card) > 21:
            print("You went over. You lose 😤")
        elif max_value == sum(list_user_card) and max_value > 16 :
            print("Opponent went over. You win 😁")
        elif max_value == sum(computer_cards) and max_value > 16:
            print("You went over. You lose 😤")
        elif sum(computer_cards) == sum(list_user_card):
            print("Draw 🙃")
        elif sum(computer_cards) == 21:
            print("Lose, opponent has Blackjack 😱")
        elif sum(list_user_card) == 21:
            print("Win, you have a Blackjack 😱")
        play_again = input("Do you want to play again? y/n ")
        if play_again == 'y':
            blackjack()
    print("Goodbye")
blackjack()