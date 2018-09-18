import urllib

def read_txt():
	open_doc = open("C:\Users\Hank2\Documents\Jeep.txt")
	reading = open_doc.read()
	open_doc.close()
	naughty_words(reading)



def naughty_words(text_to_check):
	checkity = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output =checkity.read()
	checkity.close()
	if "true" in output:
		print "Profanity Alert!"
	elif "false" in output:
		print "Clean doc!"
	else:
		print "Something wrong somewhere."

read_txt()
