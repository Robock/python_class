# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/




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





#this function lets users make a choice what level of difficulty their quizes is going to be.
# User is prompted to choose the level of difficulty for the quiz by using raw_input.
# the output of this function are the quiz text and the actual answers to the quiz.

def difficulty_level():
	first_prompt = "To select Quiz level: Type in Easy, Medium or Hard.\n"
	quiz_level = raw_input(first_prompt)   #user selection that is either easy, medium or hard
	notify_user = "\n You've selected: " + quiz_level 
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
	   incorrect_choice = "\n That's not a correct choice! Please type your choice exactly as the options presented to you."
	   print incorrect_choice
	   return difficulty_level()



#this function presents the quiz to user, compares user's answer to actual answer and fills in the 
#blanks with the correct answer until all blanks are correctly filled.
# the inputs of this function are the quiz text and the actual answers to the quiz that are
#outputted by the difficulty_level function.
#applicant is also prompted using raw_input to choose how many times to try to get the correct answer.
#the output of this function is the quiz text with the blanks filled out if user answers correctly
#or with a message letting user know the answe is not correct.  

def fill_blanks(quiz_text, quiz_answers):
	blank_index = 0
	chances = int(raw_input("\n How many times do you want to try to get the correct answer? "))
	print "\n You get to try " + str(chances) + " times."
	while blank_index < len(quiz_answers):
		user_answer = raw_input("\n Please, fill in the blank: " + str(blank_spaces[blank_index]))
		if user_answer == quiz_answers[blank_index]:
			quiz_text = quiz_text.replace(blank_spaces[blank_index], quiz_answers[blank_index])
			blank_index+=1
			print quiz_text
	
		else:
			if chances>1:
				chances-=1
				print "\n Wrong answer. Try again. You've " + str(chances) + " more chances to get it right."
			else:
				return "\n You've exhausted your chances. Good bye!"



print difficulty_level()