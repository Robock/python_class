# Quiz practice code


print "IT IS QUIZ TIME!"
print " "
print " "

'''first_prompt = "\nTo select Quiz level: Type in EASY, MEDIUM or HARD. \n"
prompt_user = raw_input(first_prompt)
print "You selected: ", prompt_user'''



#easy_quiz = "Hello __1__, I am __2__ and I like __3__."
#medium_quiz = "So far, I have learned __1__, __2__ and __3__ in this class. It is so much __4__!"
ml_string = "For this __1__, I relied on the examples from the __2__ quizes we did in the class. The project is challenging but __3__. I can't wait to complete the project __4__ and submit it soon."
#question = "What should be substituted in for:__"
parts_of_speech = ["__1__", "__2__", "__3__", "__4__"]

#answers_for_easy_quiz = ["world", "Henok", "Python"]
#answers_for_medium_quiz = ["functions", "loops", "lists", "fun"]
#answers_for_hard_quiz = ["project", "mad_lib", "doable", "successfully"]
#answer = answers_for_hard_quiz  # just to initialize the variable. It could have been assigned to any value that is higher than the blank_counter

#This function helps users chose the level of difficulty for the quiz they want to take based on user's input.
'''def game_level(user_input):
	blank_counter = 1			
    while blank_counter<=len(answer):
		  if user_input == "Easy" or user_input == "Medium" or user_input == "Hard":
		     print "You've chosen: ", user_input, " !"
		     print "Here is the Fill In The Blank Quiz."
		     if user_input == "Easy":
		    	print easy_quiz
		    	answer = answers_for_easy_quiz
		     else:
		    	 if user_input == "Medium":
		    		print medium_quiz
		    		answer = answers_for_medium_quiz
		    	 else:
		    		 if user_input == "Hard":
		    			print hard_quiz
		    			answer = answers_for_hard_quiz
		    	
		     print question, blank_counter, "__?"
		     blank_counter+=1 
		   else:
		   	    print "That's not a correct choice!"
		   	    print first_prompt'''

def word_in_pos(word, parts_of_speech):
	for pos in parts_of_speech:
		if pos in word:
			return pos
		return None


def fill_blanks(ml_string, parts_of_speech):
	replaced = []
	ml_string = ml_string.split()
	for word in ml_string:
		replacement = word_in_pos(word, parts_of_speech)
		if replacement != None:
			user_input=raw_input("Type in a: " + replacement)
			word = word.replace(replacement, user_input)
			replaced.append(word)
		else:
			replaced.append(word) 
	replaced = " ".join(replaced)
	return replaced
	print replaced


def game_level():
	
  first_prompt = "\nTo select Quiz level: Type in EASY, MEDIUM or HARD. \n"
  prompt_user = raw_input(first_prompt)
  return "You selected: ", prompt_user


#print game_level()

  if prompt_user=="Easy":
       return easy_quiz, answers_for_easy_quiz
  elif prompt_user=="Medium":
       return medium_quiz, answers_for_emedium_quiz
  elif prompt_user=="Hard":
       return hard_quiz, answers_for_hard_quiz

question, answer = game_level()
print question
print answer
fill_blanks(ml_string, parts_of_speech)



