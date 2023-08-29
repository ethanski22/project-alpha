#Title: Blackjack
import random,time # Imported random to randomize the card number

print("Type 'help' to list all commands.")

def nlprint(s): # Makes a new line after the message, so that i dont have to repeat this.
  print(s)
  print()

def help_commands():
  print("LIST OF COMAMNDS(NOT CASE SENSITIVE):")
  print()
  print("[General]")
  print("- new game|newgame|ng: Creates a new game.")
  print("- stop: Stops the program.")
  print("[In-Game]")
  print("- hit|h: Request a card.")
  print("- stay|s: Stays with hand.")
  print()

def reset_hand(): # Instead of typing each variable everytime the player wins or loses, I used a function to keep it simple.
  global play # Used global to create a global variable because if you define the variable it will become local. (Only use inside of function)
  global stay
  global hand
  global dealer
  print()
  hand=random.randint(1,11) # Random integer for the dealer/player's hands
  dealer=random.randint(1,11) # Random integer for the dealer/player's hands
  stay = False
  play = True

def reset_hand_msg(s): # Instead of typing your msg and then typing the function to reset. I made a function to do it all in one.
  print(s)
  reset_hand()

reset_hand()

while True: # Set this to true so that we can always make a new game without restarting the program.
  if play: # 'play' variable is used to create a new game.
    print("Welcome to Blackjack!")
    print("Would you like to play? (Y/N)")
    inp = input(">") # Gets the user input
    inp=inp.lower()
    print()
    if inp == "y":
      print("Current Hand:",hand)
      play = False
    elif inp == "help":
      help_commands()
		else:
			print("Program stopped")
			exit()
  else:
    if not stay:
      print()
      inp = input("([H]it/[S]tay)-->")
      inp=inp.lower() # Convert the input to lowcase so that the user doesn't have to type the command exactly.
      if inp == "h" or inp == "hit": # Instead of the user typing the full command, they can type the first letter
        hand += random.randint(1,11)
        if hand > 21:
          print("Current Hand:",hand)
          print("-Player bust. Dealer wins.")
          reset_hand()
          continue # Use 'continue' to restart the while loop instead of stopping it.
        elif hand == 21:
          print("Current Hand:",hand)
          nlprint("-Player blackjack!")
          stay = True
        print("Current Hand:",hand)
      elif inp == "s" or inp == "stay":
        nlprint("-Player stands. Dealer turn.")
        stay = True
      elif inp == "new game" or inp == "newgame" or inp == "ng":
        print("-New game being created. Please wait.")
        time.sleep(1)
        reset_hand()
        continue
      elif inp == "help":
        help_commands()
      elif inp == "stop":
        print("Program stopped.")
        reset_hand()
        continue
      else:
        print("Invalid input.")
    else:
      print("Dealer hand:",dealer)
      time.sleep(1) # Use sleep to pause the code for X amount of seconds.
      if dealer < 17: # Dealer should not hit over 16. (That's how most casinos play.)
        dealer+=random.randint(1,11)
        if dealer == 21 and hand == 21:
          print("Dealer hand:",dealer)
          print("-Dealer blackjack!")
          print("-Push. No one wins.")
          reset_hand() # Makes the game repeat by changing the variables.
          continue
        elif dealer == 21:
          print("Dealer hand:",dealer)
          reset_hand_msg("-Dealer blackjack!")
          continue
        elif dealer > 21: # If the dealer goes over 21 then bust.
          print("Dealer hand:",dealer)
          reset_hand_msg("-Dealer bust. Player wins.")
          continue
      else:
        if dealer == hand: # If the dealer and the player has equal hands then the game is a push. (DRAW)
          reset_hand_msg("-Push. No one wins.")
          continue
        elif dealer > hand: # If the dealer has a higher hand than the player then the dealer wins.
          reset_hand_msg("-Dealer wins.")
          continue
        elif dealer < hand: # If the dealer has a lower hand than the player then the dealer loses.
          reset_hand_msg("-Player wins.")
          continue
        elif hand == 21: # If the player has blackjack but not the dealer then the player wins.
          reset_hand_msg("-Player blackjack. Dealer loss.")
          continue