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

#Write your code below this line 👇
listOfOptions = [rock, paper, scissors]

me = random.choice(listOfOptions)
computer = random.choice(listOfOptions)
print(me)
print(computer)

if me == rock and computer == paper:
    print("You lost!")
if me == paper and computer == scissors:
    print("You lost!")
if me == scissors and computer == rock:
    print("You lost!")

if computer == rock and me == paper:
    print("You win!")
if computer == paper and me == scissors:
    print("You win!")
if computer == scissors and me == rock:
    print("You win!")

if computer == rock and me == rock:
    print("Draw!")
if computer == paper and me == paper:
    print("Draw!")
if computer == scissors and me == scissors:
    print("Draw!")