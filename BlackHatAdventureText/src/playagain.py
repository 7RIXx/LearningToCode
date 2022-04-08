def play_again():

	print('''
	
	Would you like to play again?
	
	 ''')
	foo = True
	deciding = 'xxx'
	while foo:
		again = input('	>>> ')
		again = list(str(again))
		if again[0].lower() == 'y':
			deciding = True
			foo = False	
		elif again[0].lower() == 'n':
			deciding = False
			foo = False
			
	return deciding
			
