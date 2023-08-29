print("welome to madlibs")
print("the spaces are in order")
print()
print("which madlibs do you want \ntype the the number of the one you want")
which = input("star wars 1, star track 2, college 3, driving test 4, video games 5: ")

if which == "1":
	import starwars
elif which == "2":
	import startrek
elif which == "3":
	import classes
elif which == "4":
	import drivingtest
elif which == "5":
	import videogames
else:
	exit()