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


import random

choice = int(input("what do u choose? Type 0 for Rock, 1 for paper or 2 for scissors \n"))
computer = random.randint(0,2)


if choice == 0:
  print(rock)
  if computer == 0:
    print(f"Computer chose: \n {rock} \n its a draw")
  elif computer == 1:
    print(f"Computer chose: \n {paper} \n You lose")
  else:
    print(f"Computer chose: \n {scissors} \n You won")
elif choice == 1:
  print(paper)
  if computer == 0:
    print(f"Computer chose: \n {rock} \n You won")
  elif computer == 1:
    print(f"Computer chose: \n {paper} \n its a draw")
  else:
    print(f"Computer chose: \n {scissors} \n You lose")
elif choice == 2:
  
  print(scissors)
  if computer == 0:
    print(f"Computer chose: \n {rock} \n You lose")
  elif computer == 1:
    print(f"Computer chose: \n {paper} \n You won")
  else:
    print(f"Computer chose: \n {scissors} \n its a draw")
else:
  print("You chose a invalid choice, You lose.")
