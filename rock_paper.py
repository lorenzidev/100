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

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

if user_input == 0:
    print("Your play: Rock")
    print(rock)
elif user_input == 1:
    print("Your play: Paper")
    print(paper)
elif user_input == 2:
    print("Your play: Scissors")
    print(scissors)

computer_response = random.randint(0,2)

if computer_response == 0:
    print("Computer Response: Rock")
    print(rock)
elif computer_response == 1:
    ("Computer Response: Paper")
    print(paper)
elif computer_response == 2:
    ("Computer Response: Scissors")
    print(scissors)

