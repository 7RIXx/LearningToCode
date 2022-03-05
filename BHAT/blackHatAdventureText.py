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
































