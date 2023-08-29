import random
print("welcome to rr")
print("you and your friends are forced to play russian rulet by a drunk russian")
print("if you refuse you will die and their will only be one survivor if you play")
playrr = input("do you still want to play: ")
if playrr == "y":
	player1 = input("Enter player 1: ")
	player2 = input("Enter player 2: ")
	player3 = input("Enter player 3: ")
	player4 = input("Enter player 4: ")
	player5 = input("Enter player 5: ")
	player6 = input("Enter player 6: ")
	num = [player1, player2, player3, player4, player5, player6]
	for x in num:
		first = num[random.randint(0,5)]
		num.remove(first)
		print(num)
		second = num[random.randint(0,4)]
		num.remove(second)
		third = num[random.randint(0,3)]
		num.remove(third)
		forth = num[random.randint(0,2)]
		num.remove(forth)
		fith = num[random.randint(0,1)]
		num.remove(fith)
		sixth = num[0]
	
	print("good, very good \nlets see who the first one out is\n...\n%s, oof that sucks for you. Ok next one is \n...\nyou, %s\nok now lets try one more\n...\n%s and %s\noops sorry about that my finger slipped\nnow there are only 2 players left lets see who survives\n...\n%s has died\n%s congrats you are the winner\n%s has been killed by the drunk russian\nhahaha there was never going to be a winner" % (first, second, third, forth, fith, sixth, sixth))

elif play == "n":
	print("im suprised you chose death instead of maybe death")
