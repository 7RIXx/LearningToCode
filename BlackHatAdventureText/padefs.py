import __main__
from time import sleep
from src.player import Player
import src.database
from PhysicalAdventure import pastrings
from src.choices import make_a_choice as mac
from src.database.checkdb import check_db
from src.database.get_backpack import get_backpack
from src.playagain import play_again
from src.printer import printer as prn
from src.database.database import backpack


def init(choices=0):
	global you
	global backpack
	you = Player(__main__.handle, [])
	backpack = get_backpack()
	intro_start_car()


# set PhysicalNarrative funcs

def intro_start_car(choices=1):
	prn(pastrings.intro_start_car_text)
	tmp = mac(choices)
	if tmp == '1':
		roadside_wait_here()


def roadside_wait_here(choices=2):
	prn(pastrings.roadside_wait_here_text)
	tmp = mac(choices)
	if tmp == '1':
		forest_approach_gate()
	elif tmp == '2':
		forest_approach_fence()


def forest_approach_gate(choices=0):
	prn(pastrings.forest_approach_gate_text)

	if check_db('lockpicks',backpack):
		forest_gate_have_lockpicks()
	else:
		prn(
			'''
		
	You go back the way you came..
	
		'''
		)
		sleep(2)
		roadside_wait_here()


def forest_gate_have_lockpicks(choices=0):
	prn(pastrings.forest_gate_have_lockpicks)
	accessed_compound()


def forest_approach_fence(choices=0):
	prn(pastrings.forest_approach_fence_text)
	if check_db('blanket',backpack):
		forest_fence_have_blanket()
	else:
		forest_fence_no_blanket()


def forest_fence_have_blanket(choices=0):
	sleep(3)
	prn(pastrings.forest_fence_have_blanket_text)
	accessed_compound()


def forest_fence_no_blanket(choices=0):
	sleep(3)
	prn(pastrings.forest_fence_no_blanket_text)
	if play_again():
		init()
	else:
		exit()


def accessed_compound(choices=2):
	prn(pastrings.accessed_compound_text)

	tmp = mac(choices)

	if tmp == '1':
		compound_approach_door()
	elif tmp == '2':
		compound_keep_looking()


def compound_approach_door(choices=0):
	prn(pastrings.compound_approach_door_text)

	if check_db('badge cloner',backpack):
		guard_room_have_cloner()
	else:
		guard_room_no_cloner()


def compound_keep_looking(choices=2):
	prn(pastrings.compound_keep_looking_text)
	tmp = mac(choices)

	if tmp == '1':
		rooftop_approach_stairwell()
	elif tmp == '2':
		rooftop_approach_vent()


def rooftop_approach_stairwell(choices=2):
	prn(pastrings.rooftop_approach_stairwell_text)

	tmp = mac(choices)
	if tmp == '1':
		rooftop_approach_vent()
	elif tmp == '2':
		accessed_compound()


def rooftop_approach_vent(choices=0):
	prn(pastrings.rooftop_approach_vent_text)

	if check_db('rope',backpack):
		rooftop_have_rope()
	else:
		rooftop_no_rope()


def rooftop_have_rope(choices=0):
	prn(pastrings.rooftop_have_rope_text)
	accessed_conference_room()


def rooftop_no_rope(choices=0):
	prn(pastrings.rooftop_no_rope_text)
	if play_again():
		init()
	else:
		exit()


def accessed_conference_room(choices=2):
	prn(pastrings.accessed_conference_room_text)
	tmp = mac(choices)

	if tmp == '1':
		elevator_push_floor_two()
	elif tmp == '2':
		elevator_push_sub_three()


def guard_room_have_cloner(choices=2):
	prn(pastrings.guard_room_have_cloner_text)
	tmp = mac(choices)

	if tmp == '1':
		elevator_push_floor_two()
	elif tmp == '2':
		elevator_push_sub_three()


def guard_room_no_cloner(choices=0):
	prn(pastrings.guard_room_no_cloner_text)
	if play_again():
		init()
	else:
		exit()


def elevator_push_floor_two(choices=2):
	prn(pastrings.elevator_push_floor_two_text)
	tmp = mac(choices)

	if tmp == '1':
		lobby_am_mikael()
	elif tmp == '2':
		lobby_am_john()


def elevator_push_sub_three(choices=1):
	prn(pastrings.elevator_push_sub_three_text)

	choice2 = 'bJuKHTft'  # stored values to allow choices to be conditionally
	choice3 = 'jIKWEdfc'  # present while mitigating likliehood to be selected
	# unless the item is present and therefore altered & shown

	# conditionally displayed options
	if check_db('rubber ducky',backpack):
		prn('''
	2. Rubber Ducky
	
	''')
		choices += 1

	if check_db('raspberry pi',backpack):
		prn('''
	3. Raspberry Pi
	
	''')
		choices += 1

	# get player choice and call proceeding function
	tmp = mac(choices)

	if tmp == '1':
		prn(pastrings.server_room_guess_text)
		sleep(3)
		mission_complete()

	elif tmp == '2':

		prn(pastrings.server_room_rubber_ducky_text)
		sleep(3)
		mission_complete()

	elif tmp == '3':

		prn(pastrings.server_room_raspberry_pi_text)
		sleep(3)
		mission_complete()


def lobby_am_mikael(choices=0):
	prn(pastrings.lobby_am_mikael_text)
	if play_again():
		init()
	else:
		exit()


def lobby_am_john(choices=0):
	prn(pastrings.lobby_am_john_text)
	sleep(3)
	elevator_push_sub_three()


def mission_complete(choices=0):

	prn(pastrings.network_access_text)
	sleep(5)

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
	root@SpaceZ:~$		''')
	sleep(3)
	print(''' 
	root@SpaceZ:~$ cd ~/Documents/Manifests/Upcoming/''')
	sleep(3)
	print('''
	root@SpaceZ:~$ cp ConfirmedNames.txt DeniedNames.txt''')
	sleep(3)
	print('''
	root@SpaceZ:~$ sudo echo {PLAYER_NAME} > ConfirmedNames.txt'''.format(PLAYER_NAME=you.handle))
	sleep(3)
	print('''
	root@SpaceZ:~$ sudo chmod 440 ConfirmedNames.txt && logout''')
	sleep(3)
	print('''
	
	
	YOUR VENGEANCE IS ETERNAL!
	
	---------------------
	
	''')
