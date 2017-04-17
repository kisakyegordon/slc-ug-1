def make_cook():
	print("Get the Ingredients")
	print("Mix")
	print("Pour Into Heated pan")
	print("Turn to other side")
	return

def make_breakfast(food, served_with):
	make_cook()
	if len(served_with) == 0:
		print("------ Yummy-----" + food )
	else:
		print("--- Yummy ---" + food)
		print("Served with"+ served_with)


make_breakfast("apple", "sauce")
