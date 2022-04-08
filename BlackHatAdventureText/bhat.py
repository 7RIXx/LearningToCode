#!/bin/python3

### ATTN 7R!Xx -- LEARN HOW TO USE THE COLOR MODULE (CRAYONS.PY) AND LEVERAGE THIS FEATURE IN MAIN ###

# PROMPT: CREATE A TEXT-ADVENTURE WHERE THE PLAYER CHOOSES HOW TO MOVE THROUGHOUT A HOUSE OF ROOMS OR SIMILAR STRUCTURE

# Plan: Make a story of branching choices via Mindly mind-mapping app, certain choices will require items, items are chosen from a list at the beginning; set a character class to hold the items; each decision/location/piece-of-narrative is its own function and the functions simply call on each other

# TODO: write the digital narrative /// put play_again feature in its own function /// put get_decision feature into its own function -- will require logic to determine the number of options available /// add user control for continue story rather than using sleep /// add sub-options to the 'guess' option in the final point of the physical narrative /// add 'go back' options to more of the areas /// add the option on play_again to re-choose inventory or leave as is

# set imports


from time import sleep
import dadefs, padefs
from src.choices import make_a_choice as mac
from src.printer import printer as prn
from src.tupu import tupu
from src.player import Player
from src.person import Person
from src.cls import cls




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

	                       A Very Special Thanks to Mr Hai

'''

intro = '''
	
	You were not chosen for the last Random Draw for Plebs to Fly in Space which was 
	put on by the bourgie SpaceZ company. Your fury knows no equal. You will ensure 
	that your name is in the upcoming draw, no matter the risk, for your vengeance 
	shall be complete and eternal.
	
	'''
	
print(pretty_banner)
sleep(3)
prn(intro)
sleep(3)







handle = input('''        

	What should the Darknet call you?
        
	>>> ''')
	
prn('''
	
	Welcome, ''' + handle + '''
	
	
	''')
sleep(2)
print('\r\n' * 15)

# CALL FOR DECISION BETWEEN PHYSICAL OR DIGITAL ATTACK VECTOR


path = 'x'
path_options = ['1','2']
while path not in path_options:
	cls()
	path = input('''

	Please select the number of your choice:

	1. Start your car 
		|
		|__/--> (Easy Mode)

	2. Turn on your computer 
		|
		|__/--> (Hard Mode)

	>>> ''')


if path == '1':

	padefs.init()
	
elif path == '2':	
	dadefs.init()

	# THE HIGHPROFILE FEATURE HERE IS NOT WORKING
	#dadefs.exploiting_firefox_admin_panel_attempt()

