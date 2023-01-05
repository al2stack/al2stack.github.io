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

rps = [rock, paper, scissors]
userchoice = int(
    input(
        "What do you choose? Tyoe 0 for rock, 1 for paper or 2 for Scissors "))
print(rps[userchoice])
compchoice = random.randint(0, 2)
print(f"Computer chose:\n {rps[compchoice]}")
if compchoice == userchoice:
    print("It's a draw")
elif userchoice == 0 and compchoice == 2:
    print("You win")
elif userchoice == 1 and compchoice == 0:
    print("You win")
elif userchoice == 2 and compchoice == 1:
    print("You win")
else:
    print("You Lose")
