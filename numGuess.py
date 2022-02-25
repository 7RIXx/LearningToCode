#!/bin/python3


# TO DO: ADD DIFFICULTY CHECK TO PLAY_AGAIN FEATURE -- TRIED TO BRING IT DOWN INTO THE WHILE LOOP BUT IT BREAKS THE FUNCTIONS ABOVE WHICH ARE RELYING ON THE SET DIFFICULTY.. I COULD DEFINE THE FUNCS IN THE WHILE, BUT THAT SEEMS SLOPPY // 

# BUGS: SOMETIMES RECEIVING LIST INDEX ERROR TRYING TO ACCESS CLUE_LIST // SEMI-FREQUENTLY HANGS UPON BOOT, RESTART TYPICALLY FIXES

# prompt: make a program in which the computer chooses a random number, then give users hints to guess the number. Every time the user guesses wrong they get another clue and their score is reduced. Example of clues: multiples of the number, divisors of the number, greater than less than


# set imports

import random
from time import sleep



# set globals

score = 120
demerits = 0
easy = False
hard = False
insane = False
stupid = False
easy_low = 10
easy_high = 100
hard_low = 100
hard_high = 1000
insane_low = 1000
insane_high = 10000
stupid_low = 100000
stupid_high = 1000000
difficulty = 'x'


# set difficulty

print("\r\n" * 2)
accept = ['e', 'h', 'i', 's']

while difficulty[0].lower() not in accept:
	difficulty = input("Easy, hard, insane, or stupid mode? ")

	if str(difficulty[0].lower()) == 'e':
		easy = True
	elif str(difficulty[0].lower()) == 'h':
		hard = True
	elif str(difficulty[0].lower()) == 'i':
		insane = True
	elif str(difficulty[0].lower()) == 's':
		stupid = True
			
	if easy is True:
		setl = easy_low
		seth = easy_high
	elif hard is True:
		setl = hard_low
		seth = hard_high
	elif insane is True:
		setl = insane_low
		seth = insane_high
	elif stupid is True:
		setl = stupid_low
		seth = stupid_high

# clue funcs: multiples , divisors, prime or no, last digit, first digit

def clue_multi(host):


	a = random.randrange(4,8)
	b = random.randrange(8,12)
	c = random.randrange(12,16)

	aa = host * a
	bb = host * b
	cc = host * c
	abc = (aa, bb, cc)
	
	multid = "Multiples of this number are: " + str(abc)

	return multid

def clue_divi(host):


	d = []

	while len(d) < 3:
		dd = random.randrange(4,31)
		if host % dd == 0 and dd not in d:
			d.append(dd)
			continue
		else:
			continue
	
	divid = "Divisors of this number are: " + str(d)
    
	return divid

def clue_first(host):

	host = str(host)
	g = host[0]

	gg = "The first digit is: " + str(g)

	return gg

def clue_last(host):

	host = str(host)
	h = host[-1]

	hh = "The last digit is: " + str(h)

	return hh

def clue_prime(host):

	primer = False
	i = 0
    
	while primer == False:
		for number in range(2,host):
			if host % number == 0:
				i += 1
		if i == 0:
			primer = True
		else:
			break
        
	primed = "Is this a prime number? " + str(primer)
	return primed
                

def ran_gen():
	
	if hard is True:
		target = random.randrange(100, 1000)
	
	elif easy is True:
		target = random.randrange(10, 100)
		
	elif insane is True:
		target = random.randrange(1000,10000)
	
	elif stupid is True:
		target = random.randrange(100000,1000000)
	
	return target

def scoreboard(score, demerits):

	display = score - demerits
	return display

def get_guess():

	guess = input("Guess a number between " + str(setl) + " and " + str(seth) + ": ")
	return guess
	


# housekeeping

pretty_banner = '''

                      #####                              
#    # #    # #    # #     # #    # ######  ####   ####  
##   # #    # ##  ## #       #    # #      #      #      
# #  # #    # # ## # #  #### #    # #####   ####   ####  
#  # # #    # #    # #     # #    # #           #      # 
#   ## #    # #    # #     # #    # #      #    # #    # 
#    #  ####  #    #  #####   ####  ######  ####   #### 

                   __ _  | \ /    __      
         |_  \/     /|_) |  X    (_  _  _ 
         |_) /     / | \ o / \>< __)(/_(_ 


'''


print(pretty_banner)
print("\r\n" + "Welcome to numGuess! Please guess a number in the range you will be given, if you get it wrong you'll be given a clue and your score will be decreased. If you hit score zero you lose." +"\r\n")


# determine the number

target = ran_gen()

multi = clue_multi(target)
divi = clue_divi(target)
first = clue_first(target)
last = clue_last(target)
prime = clue_prime(target)
clue_list = [first, last, multi, divi, prime]


# main logic loop

while score:


	print("\r\n" * 2)
	print("Current Score: " + str(scoreboard(score, demerits)))
	print("\r\n")
	guess = get_guess()

	if str(guess) == str(target):
		print("\r\n" * 2)
		print("Freak yeah, you nailed it!")
		print("\r\n" * 2)
		
		
		# Play again feature
		play_again = input("Would you like to play again? ")
		if str(play_again[0].lower()) == 'y':
			ran_gen()
			multi = clue_multi(target)
			divi = clue_divi(target)
			first = clue_first(target)
			last = clue_last(target)
			prime = clue_prime(target)
			clue_list = [first, last, multi, divi, prime]
			score = score + demerits
		else:
			print("\r\n" * 2)
			print("Thanks for playing!")
			print("\r\n" * 2)
			exit()


	else:
		print("\r\n" * 50)
		print("Nope, try again ..")
		print("\r\n")
		demerits += 20
		print("Current Score: " + str(scoreboard(score, demerits)))
		print("\r\n")
		
		# Game over feature
		if demerits == 120:
			print("\r\n")
			print("You definitely lost..")
			print("\r\n")
			
			# Play again feature
			play_again = input("Would you like to play again? ")
			if str(play_again[0].lower()) == 'y':
				ran_gen()
				multi = clue_multi(target)
				divi = clue_divi(target)
				first = clue_first(target)
				last = clue_last(target)
				prime = clue_prime(target)
				clue_list = [first, last, multi, divi, prime]
				score = score + 120
				difficulty = 'x'
			else:
				print("\r\n" * 2)
				print("Thanks for playing!")
				print("\r\n" * 2)
				exit()

				
		# Provide clue feature
		else:
			print("\r\n" * 2)
			print(clue_list[-1])
			clue_list.pop()
			






