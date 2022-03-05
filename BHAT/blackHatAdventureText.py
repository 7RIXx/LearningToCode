#!/bin/python3

# PROMPT: CREATE A TEXT-ADVENTURE WHERE THE PLAYER CHOOSES HOW TO MOVE THROUGHOUT A HOUSE OF ROOMS OR SIMILAR STRUCTURE

# Plan: Make a story of branching choices via Mindly mind-mapping app, certain choices will require items, items are chosen from a list at the beginning; set a character class to hold the items; each decision/location/piece-of-narrative is its own function and the functions simply call on each other

# TODO: write the digital narrative /// put play_again feature in its own function /// put get_decision feature into its own function -- will require logic to determine the number of options available /// add user control for continue story rather than using sleep /// add sub-options to the 'guess' option in the final point of the physical narrative /// add 'go back' options to more of the areas /// add the option on play_again to re-choose inventory or leave as is


# set imports


from time import sleep
import PhysicalNarrative.holds_physical_defs as pnd


# set globals


pretty_banner = '''

	 ******   **      **     **     **********                                             
	/*////** /**     /**    ****   /////**///                                              
	/*   /** /**     /**   **//**      /**                                                 
	/******  /**********  **  //**     /**                                                 
	/*//// **/**//////** **********    /**                                                 
	/*    /**/**     /**/**//////**    /**                                                 
	/******* /**     /**/**     /**    /**                                                 
	/**////  //      // //  ****** *******   ** **     **          ********                
	/**       **   **      //////*/**////** /**//**   **          **//////                 
	/**      //** **            /*/**   /** /** //** **   **   **/**         *****   ***** 
	/******   //***             * /*******  /**  //***   //** ** /********* **///** **///**
	/**///**   /**             *  /**///**  /**   **/**   //***  ////////**/*******/**  // 
	/**  /**   **             *   /**  //** //   ** //**   **/**        /**/**//// /**   **
	/******   **             *    /**   //** ** **   //** ** //** ******** //******//***** 
	/////    //             /     //     // // //     // //   // ////////   //////  /////

	                Special Thanks to Mr Hai and 0xCOFFEE

'''

intro = '''
	
	You were not chosen for the last Random Draw for Plebs to Fly in Space which was 
	put on by the bourgie SpaceZ company. Your fury knows no equal. You will ensure 
	that your name is in the upcoming draw, no matter the risk, for your vengeance 
	shall be complete and eternal.
	
	'''

# classes and funcs

class Player:
	# holds player name and player inventory
	def __init__(self, whoami, backpack):
		self.whoami = whoami
		self.backpack = backpack
		
def get_player():
	# gets vars to assign to player object
	pname = input('''
	
	What is your name/handle? 
	
	>>> ''')
	
	return pname
		
	
def get_inv():
	# bulk dict which personal inventory of four items will be chosen from
	cls()

	item_dict = {0:'badge cloner', 1:'blanket', 2:'raspberry pi', 3:'lockpicks', 4:'rope', 5:'cigarettes', 6:'snake camera', 7:'door shim', 8:'voice modulator', 9:'fake credentials', 10:'mars bar', 11:'rubber ducky'}
	pers_inv = []
	
	print('''
	Please choose four items to take with you from this 
	list, choose them by their assigned name and select 
	one item at a time: ''')
	space()
	print(item_dict)
	space()
	
	
	while len(pers_inv) != 4:
		x = input("I choose: ")
		if x.lower() in item_dict.values():
			pers_inv.append(x)
			cls()
			space()
			print("Current items: " + str(pers_inv))
			space()
			print(item_dict)
			space()
		elif x not in item_dict.keys():
			cls()
			space()
			print("Invalid selection.")
			space()
			print("Current items: " + str(pers_inv))
			space()
			print(item_dict)
			space()

	return pers_inv



	
# keep the readouts looking clean and distinct with both of these functions	
def space():
	print("\r\n" * 4)
	
def cls():
	print("\r\n" * 50)

# Welcome and intro

cls()
print(pretty_banner)
sleep(3)
space()
print(intro)
sleep(4)
space()

# call for decision between physical or digital attack vector
path = 'x'
path_options = ['1','2']
while path not in path_options:
	path = input('''

	Please select the number of your choice:

	1. Start your car

	2. Turn on your computer ### NOT YET BUILT ###


	>>> ''')


# Okay, we're ready for our adventure!

# Physical Adventure
if str(path) == '1':


	pnd.intro_start_car_text()

		


# Digital Adventure
elif str(path) == '2':

	space()

	print('''

	This storyline is written, but not yet built. 
	
	Please check back soon!
	
	''')

	
	path = 'x'
































