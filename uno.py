import random as r,time
print('Loading...')
print("type the card num that you want to choose")
class card():
  def __init__(self):
    self.powerchance = round(r.randint(1,11))
    if self.powerchance > 1: 
#      print('Hi'+str(self.powerchance))
      self.number = r.randint(1,10) - 1
      self.color_number = r.randint(0,3)
      self.color_list = ['GREEN','BLUE','RED','YELLOW']
      self.color = self.color_list[self.color_number]
#      print(self.number
    else:
      self.powerchance2 = r.randint(0,5)
      if self.powerchance2 == 0:
        self.card_type = 'POWERUP'
      elif self.powerchance2 == 1 or self.powerchance2 == 2:
        self.color_number = r.randint(0,3)
        self.color_list = ['GREEN','BLUE','RED','YELLOW']
        self.color = self.color_list[self.color_number]
      else:
        self.color_number = r.randint(0,3)
        self.color_list = ['GREEN','BLUE','RED','YELLOW']
        self.color = self.color_list[self.color_number]
        self.card_type = '+2'

        
  def return_values(self):
    if self.powerchance > 1:
#      print('testing'+str(self.powerchance))
      self.list = [self.color, self.number]
    elif self.powerchance2 == 0: 
      self.list = [self.card_type, '+4']
    elif self.powerchance2 == 1 or self.powerchance2 == 2:
      self.list = [self.color, 'SKIP']
    elif self.powerchance2 != 0 and self.powerchance2 != 1 and self.powerchance2 != 2:
      self.list = [self.color, self.card_type]
    return self.list

def drawcards():
  h = card()
  return h.return_values()
  
def printhand(cards):
  print ("Your hand contains the following cards: ")
  for x in range(len(cards)):
    print ("Card #" + str(x+1) + ":   " + str(cards[x]))

def think(cards, middlecard, drawing, skipturn):
  choice = -1
  print("Thinking...")
  for x in range(len(cards)):
    cardonto = cards[x]
#    print (cardonto)
    if cardonto[1] == '+4':
      choice = x
      nextdrawing = 4
      break
    elif (cardonto[1] == '+2' and cardonto[0] == middlecard[0]) or (middlecard[0] == '+2' and cardonto[0] == '+2'):
      choice = x
      nextdrawing = 2
      break
    elif (cardonto[1] == 'SKIP' and cardonto[0] == middlecard[0]) or (middlecard[0] == 'SKIP' and cardonto[0] == 'SKIP'):
      choice = x
      nextdrawing = 0
    elif cardonto[1] == middlecard[1] or cardonto[0] == middlecard[0]:
      choice = x
      nextdrawing = 0
  if choice == -1:
    choice = 'DRAW'
    nextdrawing = 0
  if drawing > 0:
    choice = 'skip'
    nextdrawing = 0
  if skipturn == True:
    return 'skip', 0 
  else:
    return choice, nextdrawing
  
def colorthink(cards):
  yellow = 0 
  red = 0 
  green = 0 
  blue = 0
  for x in range(len(cards)):
    cardonto = cards[x]
    if cardonto[0] == 'GREEN':
      green += 1
    if cardonto[0] == 'RED':
      red += 1
    if cardonto[0] == 'YELLOW':
      yellow += 1
    if cardonto[0] == 'BLUE':
      blue += 1
  colorpick = [green, blue, red, yellow]
  if max(colorpick) == green:
    return 0 
  elif max(colorpick) == blue:
    return 1 
  elif max(colorpick) == red:
    return 2 
  elif max(colorpick) == yellow:
    return 3 
    
color_list = ['GREEN','BLUE','RED','YELLOW']
cards = []

print("Which difficulty would you like to play at?")
print("Difficulty 1 - Super Easy! [Type 1 to choose]")
print("Difficulty 2 - Medium!     [Type 2 to choose]")
print("Difficulty 3 - Normal!     [Type 3 to choose]")
print("Difficulty 4 - Hard!       [Type 4 to choose]")
print("Difficulty 5 - Insane!     [Type 5 to choose]")
print("Difficulty UNKNOWN - Devil Faceoff! Warning, chances of winning are worse than winning the lottery [not calculated] ... Game will take hours! [Type 666 to choose]")
choice = int(input("Input your difficulty level here!"))
if choice == 666:
  print("Warning... This will not be good...")
  count = 50 
  count_player = 666
  print("I would wish you good luck, but no amount of luck shall help you win. Prepare for extreme lag!")
  print("Initializing... ")
else:
  count = 10 - choice
  count_player = 4 + choice
print("You start off with " + str(count_player) + " cards, and your opponents start off with " + str(count) + " cards! Good luck!")
for x in range(count_player):
  hand = card()
  cards.append(hand.return_values())
opponent1cards = []
for x in range(count):
  hand = card()
  opponent1cards.append(hand.return_values())
opponent2cards = []
for x in range(count):
  hand = card()
  opponent2cards.append(hand.return_values())
opponent3cards = []
for x in range(count):
  hand = card()
  opponent3cards.append(hand.return_values())
nextpersondraws = 0 
print("Game Initialized!")
print('')
print('')
print('')

middlecard = hand.return_values()
if middlecard[0] == 'POWERUP':
  color_number = r.randint(0,3)
  color = color_list[color_number]
print('')
print("The starting card is a " + str(middlecard))
print('')
print('')
print('')
print('Now beginning the game!')
botchoice = input("Would you like a bot to play for you? (Warning extremely fast speed!)? Type YES if desired, click ENTER if not desired.").upper()
won = 0
skipturn = False 

#MAIN LOOP

while won == 0:
  choice = 0
  if middlecard[1] == 'SKIP' and skipturn == False:
    skipturn = True
  elif middlecard[1] == 'SKIP' and skipturn == True:
    skipturn = False
  if nextpersondraws > 0:
    for x in range(nextpersondraws):
      cards.append(drawcards())
      print("You draw a card!")
    print("You just drew cards, your turn is skipped!")
    choice = 'skip'
    nextpersondraws = 0
  if middlecard[1] == 'SKIP':
    print("Sorry, but player 3 played a SKIP. Your turn is skipped!")
    choice = 'skip'
    skipturn = False
  while str(choice) != 'skip': 
    print("")
    print("")
    print("It is your turn!")
    print("The middle card is a " + str(middlecard))
    if botchoice != 'YES':
      printhand(cards)
      #for x in range(len(cards)):
      #  print("Type " + str(x+1) + " to play card #" + str(x+1))
      print("Type DRAW to draw a card (it ends your turn).")
    print ("\n")
    if botchoice != 'YES':
      choice = input()
    else:
      choice, nextpersondraws = think(cards, middlecard, nextpersondraws, skipturn)
      print(choice)
    if choice == "DRAW" or choice == 'draw' or choice == "Draw" :
      cards.append(drawcards())
      choice = 'skip'
    elif botchoice == 'YES':
      choice = int(choice)
      cardinquestion = cards[choice]
      if cardinquestion[0] == middlecard[0] or cardinquestion[1] == middlecard[1] or cardinquestion[0] == 'POWERUP':
        middlecard = cards[choice]
      if cardinquestion[1] == '+2':
            nextpersondraws = 2
      if cardinquestion[1] == '+4':
            nextpersondraws = 4
      cards.remove(cardinquestion)
      choice = 'skip'
    else:
      choice = int(choice) - 1
      
      if choice < (len(cards)) and choice > -1:
        cardinquestion = cards[choice]
        if cardinquestion[0] == middlecard[0] or cardinquestion[1] == middlecard[1] or cardinquestion[0] == 'POWERUP':
          middlecard = cards[choice]
          if cardinquestion[1] == '+2':
            nextpersondraws = 2
          if cardinquestion[1] == '+4':
            nextpersondraws = 4
          cards.remove(cardinquestion)
          choice = 'skip'
        else: 
          print("A " + str(cardinquestion) + " cannot be played on top of a " + str(middlecard))
          print("Please redo your turn!")
      else:
        print("Invalid card choice! Please redo your turn!")
  if middlecard[0] == 'POWERUP':
    if botchoice != 'YES':
      middlecard[0] = input("What color do you want?").upper()
    else:
      middlecard[0] = color_list[colorthink(cards)]
  print ("\n" * 30)
  
  if nextpersondraws > 0:
    for x in range(nextpersondraws):
      opponent1cards.append(drawcards())
      print("Opponent 1 draws a card!")
  if middlecard[1] == 'SKIP' and skipturn == False:
    skipturn = True
  elif middlecard[1] == 'SKIP' and skipturn == True:
    skipturn = False
  opponent1choice, nextpersondraws = think(opponent1cards, middlecard,nextpersondraws,skipturn)
  if opponent1choice == 'DRAW':
    opponent1cards.append(drawcards())
    print("Opponent 1 draws!")
  elif opponent1choice == 'skip':
    if skipturn != True: 
      print("Opponent 1 drew cards; their turn is skipped!")
    else: 
      print("A SKIP was played; Opponent 1's turn is skipped!")
  else:
    middlecard = opponent1cards[opponent1choice]
    print("Opponent 1 plays a " + str(middlecard))
    opponent1cards.remove(middlecard)
    if middlecard[0] == 'POWERUP':
      color_number = colorthink(opponent1cards)
      color = color_list[color_number]
      middlecard[0] = color 
      print ("They choose the color "+ color)
      
  if nextpersondraws > 0:
    for x in range(nextpersondraws):
      opponent2cards.append(drawcards())
      print("Opponent 2 draws a card!") 
  if middlecard[1] == 'SKIP' and skipturn == False:
    skipturn = True
  elif middlecard[1] == 'SKIP' and skipturn == True:
    skipturn = False
  opponent2choice, nextpersondraws = think(opponent2cards,middlecard,nextpersondraws,skipturn)
  if opponent2choice == 'DRAW':
    opponent2cards.append(drawcards())
    print("Opponent 2 draws!")
  elif opponent2choice == 'skip':
    if skipturn != True: 
      print("Opponent 2 drew cards; their turn is skipped!")
    else: 
      print("A SKIP was played; Opponent 2's turn is skipped!")
  else:
    middlecard = opponent2cards[opponent2choice]
    print("Opponent 2 plays a " + str(middlecard))
    opponent2cards.remove(middlecard)
    
    if middlecard[0] == 'POWERUP':
      color_number = colorthink(opponent1cards)
      color = color_list[color_number]
      middlecard[0] = color 
      print ("They choose the color "+ color)
      
  if nextpersondraws > 0:
    for x in range(nextpersondraws):
      opponent3cards.append(drawcards())
      print("Opponent 3 draws a card!") 
  if middlecard[1] == 'SKIP' and skipturn == False:
    skipturn = True
  elif middlecard[1] == 'SKIP' and skipturn == True:
    skipturn = False
  opponent3choice, nextpersondraws = think(opponent3cards,middlecard,nextpersondraws,skipturn)
  if opponent3choice == 'DRAW':
    opponent3cards.append(drawcards())
    print("Opponent 3 draws!")
  elif opponent3choice == 'skip':
    if skipturn != True: 
      print("Opponent 3 drew cards; their turn is skipped!")
    else: 
      print("A SKIP was played; Opponent 3's turn is skipped!")
  else:
    middlecard = opponent3cards[opponent3choice]
    print("Opponent 3 plays a " + str(middlecard))
    opponent3cards.remove(middlecard)
    
    if middlecard[0] == 'POWERUP':
      color_number = colorthink(opponent1cards)
      color = color_list[color_number]
      middlecard[0] = color 
      print ("They choose the color "+ color)
  print ("\n"*3)
  print("Opponent 1 has the following number of cards: " + str(len(opponent1cards)) + "\nOpponent 2 has the following number of cards: " + str(len(opponent2cards)) + "\nOpponent 3 has the following number of cards: " + str(len(opponent3cards)))
  if len(cards) == 0:
    won = 1
  if len(opponent1cards) == 0:
    won = 2
  if len(opponent2cards) == 0:
    won = 3 
  if len(opponent3cards) == 0:
    won = 4       
    
print ("\n" * 50)
if won == 1:
  print("Congratulations! You win!")
if won > 1:
  print("Opponent " + str(won-1) + " wins! Better luck next time!")
        
        