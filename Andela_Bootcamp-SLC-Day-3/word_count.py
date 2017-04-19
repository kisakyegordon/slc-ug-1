def word_count(input):
    """
            Python Function that counts the occurrences of words or characters in a string
    
    """
    # dictionary to hold the final answer
    group = {}

    if type(input) == str:
    	input.lower()

        # split the input 
        split_phrase = input.split()

        for i in split_phrase:

            if i in group:
            # if it already exists in the dictionary

                #dictionary converts integer string to integer
                if i.isdigit() == True:
                    i = int(i)

                    # increment value by one if it exists
                    group[i] += 1

                else:


                    # increment value by one if they exist
                    group[i] += 1

            else:
            #does not exist in our dictionary

                 # if key is a integer
                if i.isdigit() == True:
                    i = int(i)
                    group[i] = 1
                else:
                    group[i] = 1


	#Through a loop print out all items of the dictionary side by side
	for key, value in group.items():
		print key, value
	
	
word_count("I am the most Formidable of all the formidable guys you ever saw")
