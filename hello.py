#def make_breakfast():
#	print("Welcome\n These are your options for breakfast")
#	print("1. Eggs \n 2. Pancakes \n")
#	cook = input("What food do you want")
#	if cook == "eggs":
#		print("So you want eggs")

#	print("Breakfast")
#	print("1. Get the ingredients")
#	print("2. Beat the Eggs")
#	print("3. Mix any desired ingtreidients with the eggs")
#	print("4. Heat up your source of heat and heat up some cooking oil")
#	print("5. Put the ready eggs in the oil, cook, turn eggs")
#	print("6. Ready !!")
#	breakfast= "------Yummy -------" + cook
#	return breakfast

#print(make_breakfast("Egg"))
#print(make_breakfast("fISH"))
#make_breakfast();

def make_cook():
	print("Get the Ingredients")
	print("Mix")
	print("Pour Into Heated pan")
	print("Turn to other side")

def make_breakfast1(food, served_with):
	make_cook()
	if len(served_with) == 0:
		print("------ Yummy-----" + food )

make_breakfast1(eggs, sauce)
