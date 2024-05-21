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
choices = ['rock', 'paper', 'scissors']
player = input("Enter your choice. rock, paper or scissors \n")
player = player.lower()
computer = random.choice(choices)
if player == choices[0]:
    if computer == choices[1]:
        x = "you lost!"
    elif computer == choices[2]:
        x = "you won!"
    else:
        x = "Draw"
elif player == choices[1]:
    if computer == choices[0]:
        x = "you won!"
    elif computer == choices[2]:
        x = "you lost!"
    else:
        x = "Draw"
elif player == choices[2]:
    if computer == choices[0]:
        x = "you lost!"
    elif computer == choices[1]:
        x = "you won!"
    else:
        x = "Draw"
else:
    x= "choose between rock, paper, scissors plz"
if player== "rock":
    print(rock)
elif player== "paper":
    print(paper)
elif player== "scissors":
    print(scissors)
else:
    print("choose between rock, paper, scissors plz")
if computer== "rock":
    print(rock)
elif computer== "paper":
    print(paper)
elif computer== "scissors":
    print(scissors)
print(computer)
print(x)

