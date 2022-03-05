#!/bin/python3

# Collection of funcs for main program, each function will print a piece of narrative, and then print a list of choices, and then call the next func based on the user's choice

from time import sleep

def cls():
	print('\r\n' * 35)
	
def space():
	print('\r\n' * 4)
	
	
# set preperatory functions

#done, working
class Player:
	# holds player name and player inventory
	def __init__(self, whoami, backpack):
		self.whoami = whoami
		self.backpack = backpack

#done, working
def get_player():
	# gets vars to assign to player object
	pname = input('''
	
	What is your name/handle? 
	
	>>> ''')
	
	return pname
		
#done, working
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

			
	
# GOD MODE, FOR TESTING THE DECISION TREE
#pers_inv = ['badge cloner','blanket','lockpicks','rope','raspberry pi', 'rubber ducky']






# set PhysicalNarrative funcs

	


# done, working
def intro_start_car_text():


	global char
	char = Player(get_player(), get_inv())

	print(
	'''
	
	You run downstairs, fire up the engine of your Subaru Forester,
	and peel off towards SpaceZ HQ, in Balzac, Alberta

	Arriving several hours later, you pull over a block down the 
	street, where the Sun is just rising on a clear and warm Monday morning.
	
	
		1. Wait here
		
	'''
	)

	options = ['1']
	choice = 'xxx'
	while choice not in options:
		choice = input('	>> ')
	if choice == '1':
		cls()
		roadside_wait_here_text()
		

	



# done, working
def roadside_wait_here_text(): 

	print(
	'''
	
	You sit low in your vehicle until night falls. As soon as the
	shadows of dusk exceed their own absence you hop out, grab your 
	backpack, and dart off into the thick bush just off the road.

	Fifteen grueling minutes later you pop out of the bush, thorns 
	and branches are caught in your clothes and hair, and you have 
	several small cuts on your hands and face. You've arrived at the 
	rear of the compound. Ten meters to your left is a four meter tall 
	chain fence with a razor wire crown, broken only by a large gate 
	about five meters further along its length, secured by an impressive
	looking padlock.	
	
		1. Approach the gate
		
		2. Approach the fence
		
	'''
	)
	
	
	options = ['1','2']
	choice = 'xxx'
	while choice not in options:
		choice = input('	>> ')
	if choice == '1':
		cls()
		forest_approach_gate_text()
	elif choice == '2':
		cls()
		forest_approach_fence_text()



#done, working
def forest_approach_gate_text(): 


	print(
	'''
	
	The gate is secured with an impressive looking padlock.

	'''
	)
	
	if 'lockpicks' in char.backpack:
		cls()
		forest_gate_have_lockpicks()
	else:
		space()
		print(
		'''
		
	You go back the way you came..
	
		'''
		)
		space()
		sleep(2)
		roadside_wait_here_text()
		
		
		
#done, working
def forest_gate_have_lockpicks(): 

	print(
	'''
	
	Kneeling down beside the padlock you get to work picking the lock. 
	The pins are tight and you break two tensioners before you feel the 
	faint scuttle of the chamber and can exhale at the lock's release. 
	You slip in and dummy lock the pad behind you.
	
	'''
	)
	sleep(3)
	accessed_compound_text()


#done, working
def forest_approach_fence_text(): 

	print(
	'''
	
	You approach the fence at pace, launching yourself up and forward.
	Your hands grip the top bar, just below the razor wire, your feet 
	hit in the flexible spot, depressing it deeply thanks to your momentum. 
	Kicking your feet off and leveraging the rebound of the chain, you 
	vault yourself in a twisting sprial up and over ... 
	
	'''
	)
	if 'blanket' in char.backpack:
		sleep(3)
		forest_fence_have_blanket_text()
	else:
		space()
		sleep(3)
		forest_fence_no_blanket_text()
		sleep(3)
		deciding = 'xxx'
		while deciding:
			again = input('	>> ')
			again = list(str(again))
			if again[0].lower() == 'y':
				cls()
				intro_start_car_text()
			elif again[0].lower() == 'n':
				cls()
				exit()
			else:
				space()
				print("	Invalid selection")
				space()
	
	
	
#done, working
def forest_fence_have_blanket_text(): 

	print(
	'''
	
	and flip and twirl so majestically into the compound!
	
	'''
	)
	sleep(5)
	accessed_compound_text()
	
	
	
#done, working
def forest_fence_no_blanket_text(): 

	print(
	'''
	
	and right into the razor wire, where you struggle and bleed to death.
	
	YOU'RE DEAD
	
	---------------------
	
	Would you like to try again?
	
	'''
	)
	
	
	
#done, working
def accessed_compound_text(): 

	print(
	'''
	
	You stalk the shadows until you're pressed flat against the rear 
	of the building. A few meters to your left is a door with a 
	camera trained on it.
	
	
		1. Approach door
		
		2. Keep looking
		
	'''
	)
	
	options = ['1','2']
	choice = 'xxx'
	while choice not in options:
		choice = input('	>> ')
	if choice == '1':
		cls()
		compound_approach_door_text()
	elif choice == '2':
		cls()
		compound_keep_looking_text()
	
	
	
#done, working
def compound_approach_door_text(): 

	print(
	'''
	
	You edge alongside the door, just out of the camera's view, and 
	dart your hand in to test the handle.

	It's unlocked. You open it up and jolt through the camera's range 
	as quick as possible.

	Most of the lights within are dimmed. There is a room just down 
	the hall with the light on. Approaching cautiously you note the 
	guard within is sleeping in his chair! You slip inside.
	
	'''
	)
	
	if 'badge cloner' in char.backpack:
		space()
		sleep(3)
		guard_room_have_cloner_text()
	else:
		space()
		sleep(3)
		guard_room_no_cloner_text()
		sleep(3)
		deciding = 'xxx'
		while deciding:
			again = input('	>> ')
			again = list(str(again))
			if again[0].lower() == 'y':
				cls()
				intro_start_car_text()
			elif again[0].lower() == 'n':
				cls()
				exit()
			else:
				space()
				print("	Invalid selection")
				space()	

	
	
#done, working
def compound_keep_looking_text(): 

	print('''
	
	That camera presents an unacceptable risk. You migrate around the 
	corner of the building in search of alternatives.

	Running up the Northern face is a large utilities pipe, leading 
	to the roof. This is perfect! You grapple onto the conduit and 
	begin your ascent.
	
	Arriving on the roof you notice how grueling that climb actually 
	was. You're sweating profusely, breathing heavily, and can already 
	feel your muscles weaking in an attempt to recover from the 
	expenditure.
	
	Sitting down to cool off and catch your breath, you notice that 
	the roof has stairwell access, as well as some large vents.
	
	
	1. Approach stairwell
	
	2. Approach vent

	''')
	
	options = ['1','2']
	choice = 'xxx'
	while choice not in options:
		choice = input('	>> ')
	if choice == '1':
		cls()
		rooftop_approach_stairwell_text()
	elif choice == '2':
		cls()
		rooftop_approach_vent_text()
	
	
#done, working
def rooftop_approach_stairwell_text():

	print('''
	
	Approaching the stairwell, you note the door is secured with a
	badge reader. You don't have a badge right now.
	
	
	1. Approach the vent
	
	2. Climb back down
	
	''')
	
	options = ['1','2']
	choice = 'xxx'
	while choice not in options:
		choice = input('	>> ')
	if choice == '1':
		space()
		rooftop_approach_vent_text()
	elif choice == '2':
		cls()
		sleep(2)
		accessed_compound_text()
		

#done, working
def rooftop_approach_vent_text():

	print('''
	
	Looking down into the opening of this large vent, you see a big
	three-bladed fan, not currently spinning it seems. Below the
	blades is a fifty-foot drop onto the floor of what appears to be
	a conference room. To either side of the fan there are some large
	duct-openings, which you suspect lead more progressively down to
	the bottom.
	
	''')
	
	if 'rope' in char.backpack:
		space()
		sleep(6)
		rooftop_have_rope_text()
	else:
		space()
		sleep(3)
		rooftop_no_rope_text()
		sleep(3)
		deciding = 'xxx'
		while deciding:
			again = input('	>> ')
			again = list(str(again))
			if again[0].lower() == 'y':
				cls()
				intro_start_car_text()
			elif again[0].lower() == 'n':
				cls()
				exit()
			else:
				space()
				print("	Invalid selection")
				space()


#done, working
def rooftop_have_rope_text():

	print('''
	
	You pull the rope out of your backpack and tie knots into it
	every few feet, securing it to a nearby column when you're
	done.
	
	Dropping it into the vent is fairly daunting, it seems to 
	uncoil and fall for many minutes, though the real time couldn't 
	have been more than a few seconds.
	
	The descent is trying, and your forearms ache and fail to
	respond once you've released the last knot at the bottom.
	
	''')
	
	space()
	sleep(8)
	accessed_conference_room_text()


#done, working
def rooftop_no_rope_text():

	print('''
	
	You climb into the opening and, hanging by your hands, you 
	dangle your legs down and slip them into the ducting on the 
	side.
	
	Once they are in you can feel that you are in a very 
	compromised position. You don't have the strength to pull 
	back out, but you don't have the leverage to slide further 
	in.
	
	You remain static as terror grips your mind, causing your 
	blood to race, which causes your hands to sweat; and as your 
	grip moistens your hands slide free from their purchase upon 
	the vent-edge and you fall fifty-feet onto the hard tile floor 
	of the conference room.
	
	YOU'RE DEAD
	
	---------------------
	
	Would you like to try again?
	
	''')
	

#done, working
def accessed_conference_room_text():

	print('''
	
	You look around the conference room for a while, as it appears 
	to be a large and significant space for the company, and you 
	score some treasure underneath one of the several dozen 
	plastic chairs still spread across the floor from their last 
	gathering -- a badge, laying in the dust under a chair, six 
	positions in on the fourth row.
	
	Taking your treasure you continue through the building, 
	eventually arriving at an elevator, which the badge allows you 
	access to.
	
	
	1. Push "Floor Two"
	
	2. Push "Subfloor Three"
	
	''')
	
	options = ['1','2']
	choice = 'xxx'
	while choice not in options:
		choice = input('	>> ')
	if choice == '1':
		cls()
		elevator_push_floor_two_text()
	elif choice == '2':
		cls()
		elevator_push_sub_three_text()	
	
	
#done, working
def guard_room_have_cloner_text(): 

	print(
	'''
	
	Sneaking right up beside him, you feel your backpack vibrate 
	slightly -- you've cloned his badge!

	You pad back into the hallway and continue along it unobstructed 
	until you find an elevator.. Reaching into your bag you flick a 
	small switch and brush up against the elevator controls; the 
	buttons light up, you're free to maneuver.
	
	1. Push 'Floor Two'
	
	2. Push 'Sub-Floor Three'
	
	'''
	)
	
	options = ['1','2']
	choice = 'xxx'
	while choice not in options:
		choice = input('	>> ')
	if choice == '1':
		cls()
		elevator_push_floor_two_text()
	elif choice == '2':
		cls()
		elevator_push_sub_three_text()
	
	
#done, working
def guard_room_no_cloner_text(): 

	print(
	'''
	
	The guard has a badge on his belt that looks useful, you begin 
	silently to lift it free.

	As it comes off the belt you slowly look up to double check he 
	hasn't woken, and a pair of very amused eyes are the last thing 
	you see before your skull is crushed against his desk..	
	
	YOU'RE DEAD
	
	---------------------
	
	Would you like to try again?
	
	'''
	)
	
	
	
#done, working
def elevator_push_floor_two_text(): 

	print(
	'''
	
	The elevator travels smoothly and stops at floor two. The doors open 
	upon arrival, and you step out into what appears to be... A guard 
	station... These guys look like heavies -- automatic weapons and big 
	obscene blades strapped to various body parts -- private military is 
	your best guess.

	"Stop! Identify yourself!"
	
	
	1. Go big
	
	2. Go home
	
	'''
	)
	
	options = ['1','2']
	choice = 'xxx'
	while choice not in options:
		choice = input('	>> ')
	if choice == '1':
		cls()
		sleep(3)
		lobby_am_mikael_text()
		sleep(3)
		deciding = 'xxx'
		while deciding:
			again = input('	>> ')
			again = list(str(again))
			if again[0].lower() == 'y':
				cls()
				intro_start_car_text()
			elif again[0].lower() == 'n':
				cls()
				exit()
			else:
				space()
				print("	Invalid selection")
				space()
	elif choice == '2':
		cls()
		sleep(2)
		lobby_am_john_text()

	
#done, working
def elevator_push_sub_three_text(): 

	print(
	'''
	
	You exit out the elevator door directly into the aisles of a 
	server bank. Aw hullz yuh!!

	A few aisles down you encounter an access terminal.
	
	
	1. Guess
	
	'''
	)
	choice2 = 'bJuKHTft'  # stored values to allow choices to be conditionally
	choice3 = 'jIKWEdfc'  # present while mitigating likliehood to be selected
	                      # unless the item is present and therefore altered & shown
	
	# conditionally displayed options
	if 'rubber ducky' in char.backpack:
		print('''
	2. Rubber Ducky
	
	''')
		choice2 = '2'
	if 'raspberry pi' in char.backpack:
		print('''
	3. Raspberry Pi
	
	''')
		choice3 = '3'
	
	# get player choice and call proceeding function
	options = ['1','2','3']
	choice = 'xxx'
	while choice not in options:
		choice = input('	>> ')
	if choice == '1':
		cls()
		print('''
		
	You try manager:manager and the station unlocks.. Geez...
	
	Quickly accessing the terminal you setup a persistent reverse 
	shell back to a listener you left running in your Covenant instance 
	back home.
	
	''')
		sleep(6)
		space()
		sleep(4)
		mission_complete_text()
		
		# play again function
		deciding = 'xxx'
		while deciding:
			again = input('	>> ')
			again = list(str(again))
			if again[0].lower() == 'y':
				cls()
				intro_start_car_text()
			elif again[0].lower() == 'n':
				cls()
				exit()
			else:
				space()
				print("	Invalid selection")
				space()
	if choice == '2':
		cls()
		print('''
		
	You plug your Rubber Ducky into the USB port on the access 
	terminal. The code you dropped in here is an automated 
	vulnerability detector and exploiter.
	
	A few minutes go by before the screen lights up. A quick
	log check determines that the Ducky used a native backdoor
	to gain access. Quickly accessing the terminal you setup 
	a persistent reverse shell back to a listener you left running 
	in your Covenant instance back home.
	
	''')
		sleep(6)
		space()
		sleep(4)
		mission_complete_text()
		
		# play again function
		deciding = 'xxx'
		while deciding:
			again = input('	>> ')
			again = list(str(again))
			if again[0].lower() == 'y':
				cls()
				intro_start_car_text()
			elif again[0].lower() == 'n':
				cls()
				exit()
			else:
				space()
				print("	Invalid selection")
				space()
				
				
	elif choice == '3':
		cls()
		print('''
		
	Just behind this terminal you notice a switch with an available port.
	Pulling out your Raspberry Pi you jack into the port and tuck the 
	device back under a trunk of cabling.
	
	Your Covenant instance back home is set up to attempt a bind shell to
	to this device every three seconds until it connects.
	
	''')
		sleep(6)
		space()
		sleep(4)
		mission_complete_text()
		
		# play again function
		deciding = 'xxx'
		while deciding:
			again = input('	>> ')
			again = list(str(again))
			if again[0].lower() == 'y':
				cls()
				intro_start_car_text()
			elif again[0].lower() == 'n':
				cls()
				exit()
			else:
				space()
				print("	Invalid selection")
				space()

	
#done, working
def lobby_am_mikael_text(): 

	print('''
	
	"I am Mikael Farkus, CTO of SpaceZ! How many times must I remind 
	you oafs?!"

	"This guy is pretty funny, eh boys!?"

	All the guards start laughing, then one shoots you in the leg 
	while another zap straps your hand behind your back.
	
	YOU'RE INCARCERATED
	
	---------------------
	
	Would you like to try again?

	'''
	)
	
	
	
#done, working
def lobby_am_john_text(): 
	
	print('''
	
	"I'm John with Technical Security Solutions. I'm a little bit 
	lost actually, Andrew sent me back here to get some equipment 
	he forgot in the server room. Would you be able to help me find 
	where I'm supposed to go please?"

	The guards all start laughing, "For such big brains, you nerds 
	sure get confused easily. Seems like every other day we're having 
	to show you where some room or another is. Maybe you should spend 
	some time memorizing a map instead of all that computers lingo..."

	". . ."

	"Ah.. well, what do you do, eh?" he chuckles, "you want subfloor 
	three in the elevator, Champ!"

	"Alright, thank you very much, have a great night!"
	
	You step back into the elevator and hit the other button.
	
	'''
	)
	
	sleep(20)
	space()
	elevator_push_sub_three_text()
	
	
#done, working
def mission_complete_text(): 

	print('''
	
	Network Access Achieved!

	You steathily make your way back out the way you came, arriving 
	back at the Forester in about thirty minutes.

	You head straight home and sit down at your desk, you plug in 
	your super secret highly secure pass-sequence and your desktop 
	blooms before you with SHELLS EVERYWHERE AND STILL COMING IN!!!! 
	There must have been a small error in the semantics of your 
	persistance script.

	You prohibit further incoming signals, and close all but one shell.
	Leveraging some LoL tools you discover a local privesc vector and 
	gain root. Finally you can do something about this injustice! . . . 
	
	''')
	sleep(18)
	
	print('''
	
	|
	|
	~~>
	blackie@badBox:~$ fg 9675
	
	''')
	
	sleep(3)
	print('''
	root@SpaceZ:~$ passwd''')
	sleep(3)
	print('''
	root@SpaceZ:~$        ''')
	sleep(3)
	print(''' 
	root@SpaceZ:~$ cd ~/Documents/Manifests/Upcoming/''')
	sleep(3)
	print('''
	root@SpaceZ:~$ cp ConfirmedNames.txt DeniedNames.txt''')
	sleep(3)
	print('''
	root@SpaceZ:~$ sudo echo {PLAYER_NAME} > ConfirmedNames.txt'''.format(PLAYER_NAME=char.whoami))
	sleep(3)
	print('''
	root@SpaceZ:~$ sudo chmod 440 ConfirmedNames.txt && logout''')
	sleep(3)
	print('''
	
	
	YOUR VENGEANCE IS ETERNAL!
	
	---------------------
	
	Would you like to play again?	
	
	'''
	)
	
