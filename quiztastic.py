

# a quick welcome notice to the start of the quiz

print "++++++++++++++++++++++"
print "+                    +"
print "+  IT IS QUIZ TIME!  +"
print "+                    +"
print "++++++++++++++++++++++"
print " "
print " "




# three different body of text that would be presented to users to fill in the blank

easy_quiz = "Python is a widely used high-level programming __1__ for general-purpose programming, created by __2__ and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes __3__ readability, and a syntax that allows programmers to express concepts in fewer lines of __3__ than might be used in languages such as __4__ or __5__."
medium_quiz = "Artificial __1__ is a sub-field of __2__ science. Its goal is to enable the development of computers that are able to do things normally done by people. Stanford researcher John __3__ coined the term in 1956 during what is now called The __4__ conference, where the core mission of Artificial __1__ field was defined. Since then, we have seen the emergence of systems such as IBM's __5__, Google's Deep Learning and assistants like Siri, Alexa and Cortana."
hard_quiz = "Deep learning is the application of artificial neural networks (ANNs) to learning tasks that contain more than one hidden layer. Deep __1__ is part of a broader family of machine __1__ methods based on learning data representations, as opposed to task-specific algorithms. __1__ can be supervised, partially supervised or __2__. Deep learning architectures such as deep __3__ networks, deep belief __4__ and recurrent __3__ __4__ have been applied to fields including computer vision, __5__ recognition, natural language processing, audio recognition, social network filtering, machine translation and bioinformatics where they produced results comparable to and in some cases superior to human experts."



#correct answers to the blanks in the three paragraphs above.

answers_for_easy_quiz = ["language", "Guido Van Rossum", "code", "C++", "Java"]
answers_for_medium_quiz = ["intelligence", "computer", "McCarthy", "Dartmouth", "Watson"]
answers_for_hard_quiz = ["learning", "unsupervised", "neural", "networks", "speech"]



#the blank spaces organized in a list

blank_spaces = ["__1__", "__2__", "__3__", "__4__", "__5__"]



'''def you_choose():
	chances = raw_input("How many times do you want to try to get the correct answer? ")
	print "You get to try " + str(chances) + " times."
	return fill_blanks(quiz_text, quiz_answers, chances)'''




#thisfunction lets users make a choice what level of difficulty their quizes is going to be.

def difficulty_level():
	first_prompt = "To select Quiz level: Type in Easy, Medium or Hard.\n"
	quiz_level = raw_input(first_prompt)   #user selection that is either easy, medium or hard
	notify_user = "You've selected: " + quiz_level 
	print notify_user
	if quiz_level=="Easy":
		print easy_quiz
		return fill_blanks(easy_quiz, answers_for_easy_quiz)

	if quiz_level=="Medium":
		print medium_quiz
		return fill_blanks(medium_quiz, answers_for_medium_quiz)

	if quiz_level=="Hard":
		print hard_quiz
		return fill_blanks(hard_quiz, answers_for_hard_quiz)
	else:
	   incorrect_choice = "That's not a correct choice! Please type your choice exactly as the options presented to you."
	   print incorrect_choice
	   return difficulty_level()

def trys():
	chances = int(raw_input("How many times do you want to try to get the correct answer? "))
	print "You get to try " + str(chances) + " times."
	return chances

#this function presents the quiz to user, compares user's answer to actual answer and fills in the 
#blanks with the correct answer until all blanks are correctly filled.

def fill_blanks(quiz_text, quiz_answers):
	blank_index = 0
	chances = trys()
	while blank_index < len(quiz_answers):
		user_answer = raw_input("Please, fill in the blank: " + str(blank_spaces[blank_index]))
		if user_answer == quiz_answers[blank_index]:
			quiz_text = quiz_text.replace(blank_spaces[blank_index], quiz_answers[blank_index])
			blank_index+=1
			print quiz_text
	
		else:
			if chances>1:
				chances-=1
				print "Wrong answer. Try again. You've " + str(chances) + " more chances to get it right."
			else:
				return "You've exhausted your chances. Good bye!"



print difficulty_level()

