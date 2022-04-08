from time import sleep
from src.cls import cls


def printer(string):

	# tool for printing strings letter by letter, while contained within some given margins for aesthetic purposes
	# margins solved via multi-line string formatting, this will follow the format the text is set in
	text = string
	my_list = []
	for letter in text:
		
		my_list.append(letter)
		show_list = ''.join(my_list)
		sleep(0.04)  #DEFAULT 0.04
		cls()
		print(show_list)
		
		
		
		
if __name__ == "__main__":
	x = 	'''	
	This is a super cool printing tool
	that is pretty badass and will save
	the trouble of using time.sleep to predict how
	long a given player might need to 
	read 
	some 
	given 
	text!
	'''
	printer(x)
