import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []
user_score = 0
computer_score = 0

is_game_over = False
blackjack_score = 21

play_or_not = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


def add_to_user_cards(user_cards_list):
    user_cards_list.append(random.randint(1, 11))
    return user_cards_list


def calculate_player_score_after_player_choice(user_cards_, user_score_):
    user_score_ += user_cards_[-1]
    return user_score_


def check_score(user_score_, computer_score_):
    if user_score_ > 21 > computer_score_:
        return "You went over. You lose :("
    elif user_score_ == 21 and computer_score_ == 21:
        return "Draw!"
    elif user_score_ < 21 and computer_score_ < 21:
        if user_score_ > computer_score_:
            return "You win!"
    elif user_score_ == 21 and computer_score_ < 21:
        return "You got a blackjack! You win!"
    elif computer_score_ == 21 and user_score_ < 21:
        return "Computer got a blackjack! You lose!"


while not is_game_over:
    user_cards.append(random.randint(1, 11))
    user_cards.append(random.randint(1, 11))

    user_score += sum(user_cards)

    computer_cards.append(random.randint(1, 11))
    computer_cards.append(random.randint(1, 11))

    computer_score += sum(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    player_choice = input("Type 'y' to get another card, type 'n' to pass: ")

    while player_choice == 'y':
        updated_user_card_list = add_to_user_cards(user_cards)
        print(f"Your cards: {updated_user_card_list},"
              f" current score: {calculate_player_score_after_player_choice(user_cards, user_score)}")
        print(f"Computer's first card: {computer_cards[0]}")
        print(check_score(user_score, computer_score))

        player_choice = input("Type 'y' to get another card, type 'n' to pass: ")

    if player_choice == 'n':
        while computer_score < 16:
            computer_cards.append(random.randint(1, 11))
            computer_score += computer_cards[-1]
        print(check_score(user_score, computer_score))

    is_game_over = True
    # print(user_cards, computer_cards)
