import time
import random
print("MONEY MADNESS")
time.sleep(3)
print("You have to enter for rock, paper and scissor. You have to earn double of your initial amount by betting an amount for the next round.")
time.sleep(1)
initial_amount = int(input("Enter your initial amount: "))
amount = initial_amount
time.sleep(1)
game_list = ["rock", "paper", "scissor"]
while amount != 2 * initial_amount:
  time.sleep(2)
  think = random.choice(game_list)
  choice = input("Enter rock, paper or scissor: ")	
  time.sleep(1)
  bet = int(input("Enter your bet: "))
  time.sleep(2)
  if bet > amount:
    bet = int(input(f"Enter an amount smaller than {amount + 1}: "))
  if bet == 0:
    bet = int(input("You cannot bet a zero. Enter your bet: "))
  time.sleep(2)
  print(f"I played {think}!")
  time.sleep(2)	
  if (think == "rock" and choice == "paper") or (think == "paper" and choice =="scissor") or (think == "scissor" and choice == "rock"):
    amount = amount + bet
    if amount == 2 * initial_amount:
	    print("Congratulations! You won!")
	    break
    print(f"Yay! You won this round! You currently have {amount} dollars.")
    continue
  if (think == "paper" and choice == "rock") or (think == "scissor" and choice =="paper") or (think == "rock" and choice == "scissor"):
    amount = amount - bet
    if amount == 0:
      print("You have become bankrupt!")
      break
    print(f"You lost this round! You currently have {amount} dollars.")
    continue	
  if think == choice:
    print(f"Nobody wins this round! You currently have {amount} dollars.")
    continue