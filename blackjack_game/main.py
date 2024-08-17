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


def add_to_computer_cards(computer_cards_list, computer_score_):
    while computer_score_ <= 16:
        computer_cards_list.append(random.randint(1, 11))
        computer_score_ = sum(computer_cards_list)
    return computer_cards_list


def calculate_computer_score(computer_cards_, computer_score_):
    computer_score_ += computer_cards_[-1]
    return computer_score_


# def check_result(user_score_, computer_score_):
#     if computer_score_ == blackjack_score:
#         return "You lose!"
#     if user_score_ == blackjack_score and computer_score_ != blackjack_score:
#         return "You win! :)"
#     if computer_score_ > 21:
#         return "You win!"
#     if user_score > 21:
#         return "You lose!"

def score_checker(user_score_, computer_score_):
    if computer_score_ == blackjack_score:
        return "Computer wins!"
    if user_score_ == blackjack_score and computer_score_ != blackjack_score:
        return "You win!"
    if user_score_ > 21:
        return "You went over! You lose!"
    if computer_score_ > 21:
        return "Computer went over! You win."
    if 21 > user_score_ == computer_score_ < 21:
        return f"Draw!"
    if computer_score_ > user_score_:
        return "Computer wins!"
    if user_score_ > computer_score_:
        return "You win!"


def final_stats_output():
    return (f"Your final hand: {user_cards}, final score: {user_score}"
            f"\nComputer's final hand: {computer_cards}, final score: {computer_score}")


# while not is_game_over:
#     user_cards.append(random.randint(1, 11))
#     user_cards.append(random.randint(1, 11))
#
#     user_score += sum(user_cards)
#
#     computer_cards.append(random.randint(1, 11))
#     computer_cards.append(random.randint(1, 11))
#
#     computer_score += sum(computer_cards)
#
#     print(f"Your cards: {user_cards}, current score: {user_score}")
#     print(f"Computer's first card: {computer_cards[0]}")
#
#     player_choice = input("Type 'y' to get another card, type 'n' to pass: ")

user_cards.append(random.randint(1, 11))
user_cards.append(random.randint(1, 11))

user_score += sum(user_cards)

computer_cards.append(random.randint(1, 11))
computer_cards.append(random.randint(1, 11))

computer_score += sum(computer_cards)

print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {computer_cards[0]}")

player_choice = input("Type 'y' to get another card, type 'n' to pass: ")

while player_choice == 'y' and not is_game_over:
    updated_user_cards_list = add_to_user_cards(user_cards)
    user_score = calculate_player_score_after_player_choice(updated_user_cards_list, user_score)
    print(f"Your cards: {updated_user_cards_list},"
          f" current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == blackjack_score or user_score > 21:
        print(final_stats_output())
        print(score_checker(user_score, computer_score))
        is_game_over = True

    if not is_game_over:
        player_choice = input("Type 'y' to get another card, type 'n' to pass: ")

if player_choice == 'n' and not is_game_over:
    updated_computer_cards_list = add_to_computer_cards(computer_cards, computer_score)
    computer_score = calculate_computer_score(updated_computer_cards_list, computer_score)
    print(final_stats_output())
    print(score_checker(user_score, computer_score))
    is_game_over = True


