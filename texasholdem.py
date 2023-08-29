import random,time

def nlprint(s):
  print(s)
  print()

print("LIST OF COMAMNDS(NOT CASE SENSITIVE):")
print()
print("type 'fold' to end the program")
print()

def reset_hand():
	global play 
	global stay
	global hand
	global dealer
	print()
	# sets card values
	stay = False
	play = True

def reset_hand_msg(s): 
  print(s)
  reset_hand()

reset_hand()

while True:
	if play:
		print("welcome to texas holdem")
		print("Would you like to play? (Y/N)")
		x=str(input())
		x=x.lower()
		print()
		if x == "y":
			hand1=random.randint(1,13)
			hand2=random.randint(1,13)
			table1=random.randint(1,13)
			table2=random.randint(1,13)
			table3=random.randint(1,13)
			table4=random.randint(1,13)
			table5=random.randint(1,13)
			
			print("Your hand: " + str(hand1) + " " + str(hand2))
			print("Cards on the table: " + str(table1) + " " + str(table2))
			print("do you want to bet check or fold?")
			bet1 = str(input())
			bet1 = bet1.lower()
			if bet1 == "bet":
				print("how much")
				aaf = input()
			elif bet1 == "check":
				print()
			elif bet1 == "fold":
				exit()
			else:
				exit()
			if bet1 == "bet" or "check":
				print("new cards on the table: " + str(table1) + " " + str(table2) + " " + str(table3))
				print("do you want to bet check or fold?")
				bet2 = str(input())
				bet2 = bet2.lower()
				if bet2 == "bet":
					print("how much")
					aaaf = input()
				elif bet2 == "check":
					print()
				elif bet2 == "fold":
					exit()
				else:
					exit()
				if bet2 == "bet" or "check":
					print("new cards on the table: " + str(table1) +  " " + str(table2) + " " + str(table3) + " " + str(table4))
					print("do you want to bet check or fold?")
					bet3 = str(input())
					bet3 = bet3.lower()
					if bet3 == "bet":
						print("how much")
						af = input()
					elif bet3 == "check":
						print()
					elif bet3 == "fold":
						exit()
					else:
						exit()
					if bet3 == "bet" or "check":
						print("Your hand: " + str(hand1) + " " + str(hand2))
						print("new cards on the table: " + str(table1) + " " + str(table2) + " " + str(table3) + " " + str(table4) + " " + str(table5))
			cards = [hand1, hand2, table1, table2, table3, table4, table5]
			
		elif x == "n":
			exit()
		else:
			exit()