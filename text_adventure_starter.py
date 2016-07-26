start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''
left = False
leftFate = "You decide to go left and find yourself outiside, faced by a large lake. You can choose to try to swim across the lake or walk around"
rightFate = "You choose to go right and find yourself in a dark hallway with a staircase. Do you want to go up the staircase or keep walking down the hallway?"
swimmingFate = "You swam across the lake, but as you were getting out you see a cute dog running away. Do you want to follow the dog?"
walkingFate = "You attempt the long walk around the lake, and realize swimming was the quicker route, but you eventually reach a beach, and as you approach it you see a small cat running away. Do you want to follow the cat?"
stairFate = "You go up the stairs to find yourself on a beach, as your getting out you see a cute dog running away. Do you want to follow the dog?"
hallFate = "You keep walking down the hall and find yourself at a lake. You can choose to try to swim across the lake or walk around"
endScreen = "Congratulations! You finished the story, good choice following the dog because he was your quickest route to the end"
endScreen2 = "You walk a little on the beach and reach a platform. Congratulations! You finished the story, good choice going your own way, you got the quickest route to the end "
almostEndScreen = "You keep trekking up the beach and eventually you reach the end of your story, however, you should have followed the dog, you took an overly long route to the end."
almostEndScreen2 = "You follow the cat but he takes you on a longer and more treacherous route than necessary. You should have go on your own way, however you do eventually reach the end of the story."

print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
	print(leftFate)
	swimOrWalk = input("Type 'swim' to swim accross or type 'walk' to walk around it")
	if swimOrWalk == "swim":
		print (swimmingFate)
		swimmingChoice = input("Type 'yes' to follow the dog, type 'no' to go your own way.")
		if swimmingChoice == "yes" :
			print (endScreen)
		elif swimmingChoice == "no" :
			print (almostEndScreen)
	elif swimOrWalk == "walk" :
		print (walkingFate)
		walkingChoice = input("Type 'yes' to follow the cat, type 'no' to go your own way.")
			if walkingChoice == "yes" :
				print (almostEndScreen2)
			elif walkingChoice = "no" :
				print (endScreen2)
    #done = True
elif user_input == "right":
    print(rightFate) # finished the story writing what happens
	stairsOrNot = input ("Type 'stairs' to walk up the staircase or type 'hall' to continue down the hall")
		if stairsOrNot == "stairs" :
			print(stairFate)
			stairsChoice = input("Type 'yes' to follow the dog, type 'no' to go your own way.")
			if stairsChoice == "yes" :
				print (endScreen)
			elif stairsChoice == "no" :
				print (almostEndScreen)
		elif stairsOrNot == "hall" :
			print(hallFate)
			swimOrWalk = input("Type 'swim' to swim accross or type 'walk' to walk around it")
			if swimOrWalk == "swim":
				print (swimmingFate)
				swimmingChoice = input("Type 'yes' to follow the dog, type 'no' to go your own way.")
				if swimmingChoice == "yes" :
					print (endScreen)
				elif swimmingChoice == "no" :
					print (almostEndScreen)
			elif swimOrWalk = "walk" :
				print (walkingFate)
				walkingChoice = input("Type 'yes' to follow the cat, type 'no' to go your own way.")
				if walkingChoice == "yes" :
					print (almostEndScreen2)
				elif walkingChoice = "no" :
					print (endScreen2)
			
    #done = True
	

