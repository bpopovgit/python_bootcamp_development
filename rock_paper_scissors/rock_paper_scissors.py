import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possible_choices = [0, 1, 2]

game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

while player_choice not in possible_choices:
    print("Invalid choice! Please choose again.")
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(game_images[player_choice])

computer_choice = random.choice(possible_choices)

print(f"Computer chose: ")
print(game_images[computer_choice])

if player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose!")
elif computer_choice > player_choice:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")
elif player_choice == computer_choice:
    print("It's a draw!")
