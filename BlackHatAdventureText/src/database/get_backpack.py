# backpack getter

from src.database.database import closet

def get_backpack():
	# bulk dict which personal inventory of four items will be chosen from
	backpack = []
	

	
	y = 1
	while len(backpack) != 4:
		print('\r\n' * 25)
		print('''
	
	Please choose four items to take with you from this 
	list, choose them by their assigned name and select 
	one item at a time: 
	
	''')
		print(str(closet) + '\r\n\r\n' + 'Backpack: ' + str(backpack) + '\r\n\r\n')
		x = input("I choose: ")
		if x.lower() in closet:
			backpack.append(x)
			y += 1
			print('\r\n' * 10)
			print("Current items: " + str(backpack))
			print('\r\n')
			print(closet)
			print('\r\n')
		elif x.lower() not in closet:
			print('\r\n')
			print("Invalid selection.")
			print('\r\n')
			print("Current items: " + str(backpack))
			print('\r\n')
			print(closet)
			print('\r\n')

	return backpack
	
	
if __name__ == '__main__':

	get_backpack()
