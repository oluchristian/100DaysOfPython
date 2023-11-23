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
game_images = [rock, paper, scissors]
rand = random.randint(0, 2)


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#Print the user's choice and the computer's choice
print(f"Your choice:\n{game_images[user_choice]}\nComputer's choice: \n{game_images[rand]}\n")
#Rules for rock paper scissors
if user_choice >= 0 and user_choice <= 2:
  if (user_choice == 0 and rand == 1) or (user_choice == 1 and rand == 2) or (user_choice == 2 and rand == 0):  
    print("You lost")
  elif (user_choice == rand):
    print("It is a tie")
  else:
    print("You won")
else:
  print("Incorrect input. Try again")