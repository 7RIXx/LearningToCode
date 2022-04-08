# seems to be working now
def make_a_choice(number_of_choices:int):
	
	choice = 'x'
	options = []
	for x in range(1,number_of_choices+1):
		options.append(str(x))
		
	while choice not in options:
		
		choice = input('''
    
	Select the integer of your demise!
    
	>>> ''')
	
	return choice
	
