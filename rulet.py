import random,time
empty = False
print('''Welcome to my game.
  The original game: https://repl.it/@ZobDuTurfu/Roulette-Game
  This is a remake with some new feature, but check out the original game!
    Hope you enjoy my game!''')
def clear():
  print('\n'*15)
print('What do you wanna do? (Tutorial, Start)')
mode = input()
while mode != 'Start':
  if mode == 'Tutorial':
    print('\n'*3)
    print('You are in a casino to bet your money.')
    print('You start with $100, and your mission is to get $5000 to win.')
    print('You will need to enter your bet amount, then type what you are bet in.')
    print('''Options to bet are:
     - Red or Black: This will double your bet if you win.
     - Number from 1 - 36: This will make your bet worth 20 times if you win.''')
    time.sleep(3)
    print('Press [Enter] to close this tutorial.')
    n = input()
    if n == '':
      clear()
      print('What do you wanna do? (Tutorial, Start)')
      mode = input()
  else:
    print('\n')
    print('Only enter \'Tutorial\' or \'Start\', please.')
    print('What do you wanna do? (Tutorial, Start)')
    mode = input()
money = 100
while money < 5000:
  print('\n' * 3)
  print('You have: $%s' % money)
  if money == 0:
    empty = True
    break
  bet_amount = int(input('Bet: '))
  while bet_amount > money:
    print('\n')
    print('You don\'t have enough money.')
    print('\n')
    bet_amount = int(input('Bet: '))
  money -= bet_amount
  bet = input('Bet on what? Number or Color? ')
  if bet == 'Number':
    print('\n')
    final_bet = int(input('What number do you bet on? '))
    if 1 <= final_bet <= 36:
      print('The roulette is spinning...')
      time.sleep(3)
      k = random.randint(1, 37)
      print('It\'s number %s.' % k)
      if k == final_bet:
        print('Congratulations!You\'ve won 20 times your bet!')
        money += bet_amount * 20
      else:
        print('Oh no, you\'ve lost this time. Good luck next time!')
    else:
      print('Your number you bet on is unavailable. Please bet again!')
      money += bet_amount
  elif bet == 'Color':
    print('\n')
    final_bet = input('What color do you bet on? ')
    if final_bet == 'Black' or final_bet == 'Red':
      print('The roulette is spinning...')
      time.sleep(3)
      k = random.choice(['Red', 'Black'])
      print('The roulette lands on %s.' % k)
      if k == final_bet:
        print('You\'won 2 times your bet! Well done!')
        money += bet_amount * 2
      else:
        print('Unfortunately, you\'ve lost this time. Hope you won next time!')
    else:
      print('At the moment, your bet is unavailable. Please bet again, please.')
      money += bet_amount
  else:
    print('You wasn\'t bet for this turn because you choose something other than Number and Color. Let\'s re-bet!')
    money += bet_amount
if empty == False:
  print('\n')
  print('By being a millionare, you\'ve earn $100 and you retired.')
  print('\n')
  print('Before you retire, you\'ve sent $%s to charity. Good job!' % (money - 4900))
  print('\n')
  print('You have won this roulette game. Take screenshot of this game and you\'ll be one of our champions!')
else:
  print('You have no money left. You have nothing left to eat and then you die. Good luck next time.')
