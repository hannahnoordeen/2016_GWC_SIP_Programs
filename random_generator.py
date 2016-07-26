import random

decision = "hello"

while decision != "quit":
	decision = input("\n Would you like a list of dishes, bands, drinks, boy names, or girl names (Type 'quit' to quit)? ")

	if decision == "dishes":
		first_list = ["Spicy", "Hot", "Seasoned", "Creamy", "Delicate", "Flavorful", "Juicy", "Indulgent", "Rich", "Delicious"]
		second_list = ["steamed", "diced", "grilled", "pan-seared", "deep-fried", "barbequed", "wok-fried", "marinated", "slow-roasted", "italian"]
		third_list = ["noodles", "vegetables", "pasta", "chicken", "fish", "burger", "sliders", "lamb", "chicken wings", "steak"]

		print("\n" + "Menu: " + "\n")
		x = 1
		for i in range (10):
			word1 = first_list[random.randint(0, len(first_list) - 1)]	
			word2 = second_list[random.randint(0, len(second_list) - 1)]
			word3 = third_list[random.randint(0, len(second_list) - 1)]
			
			print( "{}. ".format(x) + word1 + " " + word2 + " " + word3 + "\n")
			x+=1
			
			first_list.remove(word1)
			second_list.remove(word2)
			third_list.remove(word3)
		
	elif decision == "bands":
		first_list = ["Crazy", "Hot", "Running", "Dreamy", "Loud", "Amazing", "Mystical", "Peaceful", "Angry", "Happy"]
		second_list = ["Brothers", "Trees", "Chairs", "Beauties", "Sisters", "Family", "Voices", "People", "Musicians", "Party Animals"]

		print("\n" + "Bands: " + "\n")
		x = 1
		for i in range (10):
			word1 = first_list[random.randint(0, len(first_list) - 1)]	
			word2 = second_list[random.randint(0, len(second_list) - 1)]
			
			print( "{}. ".format(x) + "The " + word1 + " " + word2 + "\n")
			x+=1
			
			first_list.remove(word1)
			second_list.remove(word2)
		
	elif decision == "drinks":
		first_list = ["Hot", "Cold", "Bubbly", "Fizzy", "Sweet", "Thick", "Thin", "Foamy", "Healthy", "Delicious"]
		second_list = ["cherry", "vanilla", "grape", "orange", "lemon-lime", "strawberry", "banana", "cantaloupe", "grapefruit", "chocolate"]
		third_list = ["tea", "soda", "cola", "water", "iced tea", "energy drink", "smoothie", "milshake", "milk", "sparkling water"]

		print("\n" + "Drinks: " + "\n")
		x = 1
		for i in range (10):
			word1 = first_list[random.randint(0, len(first_list) - 1)]	
			word2 = second_list[random.randint(0, len(second_list) - 1)]
			word3 = third_list[random.randint(0, len(second_list) - 1)]
			
			print( "{}. ".format(x) + word1 + " " + word2 + " " + word3 + "\n")
			x+=1
			
			first_list.remove(word1)
			second_list.remove(word2)
			third_list.remove(word3)
			
	elif decision == "boy names":
		last_name = input("\nEnter your last name: ")
		first_list = ["Robert", "John", "Steve", "Craig", "Greg", "Roger", "George", "Henry", "Bill", "Donald"]
		second_list = ["Chris", "Christian", "Colin", "Samuel", "Jared", "Brandon", "James", "Aaron", "Owen", "Andrew"]

		print("\n" + "Boy names: " + "\n")
		x = 1
		for i in range (10):
			word1 = first_list[random.randint(0, len(first_list) - 1)]	
			word2 = second_list[random.randint(0, len(second_list) - 1)]
			
			print( "{}. ".format(x) + word1 + " " + word2 + " " + last_name + "\n")
			x+=1
			
			first_list.remove(word1)
			second_list.remove(word2)
			
	elif decision == "girl names":
		last_name = input("\nEnter your last name: ")
		first_list = ["Hannah", "Rebecca", "Emily", "Lauren", "Sarah", "Samantha", "Jennifer", "Nicole", "Mary", "Kelly"]
		second_list = ["Michelle", "Lindsay", "Kate", "Anne", "Sophia", "Veronica", "Marie", "Elizabeth", "Lisa", "Jessica"]

		print("\n" + "Girl names: " + "\n")
		x = 1
		for i in range (10):
			word1 = first_list[random.randint(0, len(first_list) - 1)]	
			word2 = second_list[random.randint(0, len(second_list) - 1)]
			
			print( "{}. ".format(x) + word1 + " " + word2 + " " + last_name + "\n")
			x+=1
			
			first_list.remove(word1)
			second_list.remove(word2)
	
	elif decision == "quit":
		print("\nThanks for using the random generator!")