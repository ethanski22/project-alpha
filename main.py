print("hello there " + input("what is your name: "))
print("do you want to play a game?(Y/N)")
print("my games are not case sensitive")
print("there will be no money because this is a school project")
x = str(input())
x=x.lower()
if x == "y":
	print("good, very good")
elif x == "n":
	print("Why?")
	y = str(input())
	print("oh i see")
	exit()
else:
	print("unexpected input: ")
	exit()
print("what game do you want to play?")
z = input("blackjack : 1\n5 card poker : 2\nrulet : 3\ntexas holdem : 4\nuno : 5\nmad libs : 6\ncalculator : 7\nmy scheduel : 8\n")
if z == "1":
	print("blackjack it is")
	import blackjack
elif z == "2":
	print("5 card poker it is")
	import fivecardpoker
elif z == "3":
	print("rulet it is")
	import rulet
elif z == "4":
	print("texas holdem it is")
	import texasholdem
elif z == "5":
	print("uno it is")
	import uno
elif z == "6":
	print("mad libs it is")
	import madlibs
elif z == "7":
	import calc
elif z == "8":
	import mycalandar
elif z == "rr":
	import rr
else:
	print("no u")
	exit()