from .person import Person

class Player(Person):
	def __init__(self,name,backpack=[]):
		# you should feed the inventory selection dict here
		self.backpack = backpack
		self.handle = name
	
	

        
        
        
        
if __name__ == '__main__':

	backpack = {1:'test', 2:'unit', 3:'predHunter', 4:'liquid skin'}
	tonytiger = Player(backpack)


	
	print(tonytiger.backpack)
	print(tonytiger.handle)
