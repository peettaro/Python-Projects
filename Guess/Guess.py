
# CREATING A GUESSING GAME TO PLAY
# IMPORTING NECESSARY MODULES
import random

def guess_game():
# CREATING THE OPTIONS LIST
	list_of_words = ["elephant", "giraffe", "rhino", "monkey", "zebra", "hippo", "lion", "buffallo", "goat", "sheep"]

# RANDOMLY PCIKING A NAME
	selected = random.randint(0, 11)

	count = 1
	chances = 3
# PRINTING OUT THE OPTIONS
	print("Hey there :-), welcome to the guessing game!!!. Guess from the names below which one i am thinking of:")
	for i in list_of_words:
		print("{} : {}".format("*", i))

	try:
		user_in = input("Enter the name i am thinking of, this is trial {}/3: ".format(str(count)))
	except Exception as e:
		print("You have an error, {}".format(e))

# CREATING THE INPUT LOOP
	while user_in != list_of_words[selected] and count < chances:
		print("Wrong guess, try again!!!")
		count += 1
		try:
			user_in = input("Enter the name i am thinking of, this is trial {}/3: ".format(str(count)))
		except Exception as e:
			print("You have an error, {}".format(e))

# OUTPUT WHEN USER_IN IS CORRECT
	if user_in == list_of_words[selected]:
		print("Good work, you got the answer!!! with {} trial(s)".format(str(count)))

# OUTPUT WHEN CHANCES RUN OUT
	else:
		print("Sorry, ran out of chances!!!!")
		print("The answer was {}".format(list_of_words[selected]))

# EXCECUTING THE FUNCTION
if __name__ == "__main__":
	guess_game()







