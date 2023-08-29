import random,time

def nlprint(s):
  print(s)
  print()

print("LIST OF COMAMNDS(NOT CASE SENSITIVE):")
print()
print("request cards:(amount of cards, up to 3)")
print("the first card is card 1 the second is 2 and so on")
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
		print("welcome to 5 card poker")
		print("Would you like to play? (Y/N)")
		x=str(input())
		x=x.lower()
		print()
		if x == "y":
			hand1=random.randint(1,14)
			hand2=random.randint(1,14)
			hand3=random.randint(1,14)
			hand4=random.randint(1,14)
			hand5=random.randint(1,14)
			hand1=random.randint(1,14)
			rhand1=random.randint(1,14)
			rhand2=random.randint(1,14)
			rhand3=random.randint(1,14)
			
			print("Current hand: " + str(hand1) + " " + str(hand2) + " " + str(hand3) + " " + str(hand4) + " " + str(hand5))
			print("which cards do you want to get rid of?(up to 3)")
			print("print one at a time please")
			print("print 0 in you want no cards")
			c1 = str(input())
			
			if c1 != "0":
				if c1 == "0":
					print()
				elif c1 == "1":
					hand1 = rhand1
				elif c1 == "2":
					hand2 = rhand1
				elif c1 == "3":
					hand3 = rhand1
				elif c1 == "4":
					hand4 = rhand1
				elif c1 == "5":
					hand5 = rhand1
				else:
					exit()
				print("do you want a second card?(Y/N)")
				p = str(input())
				p = p.lower()
				if p == "y":
					print("what other card?")
					c2 = str(input())
					if c2 == "0":
						print()
					elif c2 == "1":
						hand1 = rhand2
					elif c2 == "2":
						hand2 = rhand2
					elif c2 == "3":
						hand3 = rhand2
					elif c2 == "4":
						hand4 = rhand2
					elif c2 == "5":
						hand5 = rhand2
					else:
						exit()
					if c2 != 0:
						print("do you want a third card?(Y/N)")
						p1 = str(input())
						p1 = p1.lower()
						if p1 == "y":
							print("what other card?")
							c3 = str(input())
							if c3 == "0":
								print()
							elif c3 == "1":
								hand1 = rhand3
							elif c3 == "2":
								hand2 = rhand3
							elif c3 == "3":
								hand3 = rhand3
							elif c3 == "4":
								hand4 = rhand3
							elif c3 == "5":
								hand5 = rhand3
							else:
								exit()
						elif p1 == "n":
							print()
			elif c1 == 0:
				print()
			else:
				print()
			print("New hand: " + str(hand1) + " " + str(hand2) + " " + str(hand3) + " " + str(hand4) + " " + str(hand5))
		elif x == "n":
			exit()
		else:
			print()
		original = [hand1, hand2, hand3, hand4, hand5]
		count = 0
		pair = 0
		for t in original:
			for f in original:
				if t == f:
					count += 1
					if count >= 2:
						#print("pair" / 2)
						pair += 1
			count = 0
		pair1 = str(pair / 2)
		print()
		print("total pairs " + pair1)
		print()