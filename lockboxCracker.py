#!/bin/python3


'''

A particular type of masterkey lockbox I was using has a ten button combination system. During the course of a particular conversation I was informed that "the order does not matter with this type of box." I tested it on several boxes and found this person's declaration was true! That simple fact brings into the realm of possibility a full bruteforce attack of this system by some given person. Exactly how in scope would such an attack be?

Counting key combos in my head was becoming frustrating, so I decided to write this code snippet to calculate the approximate possible combinations should someone decide to bruteforce one of these boxes.


Citations: 

1) https://www.codingem.com/python-how-to-get-all-combinations-of-a-list/
2) https://docs.python.org/3/library/itertools.html

'''

# IMPORTS	

import itertools
from time import sleep

# GLOBALS

buttons = [1,2,3,4,5,6,7,8,9,0] ## CHANGE ME TO A LIST OF CUSTOM BUTTONS

comLen = 4 ## CHANGE ME TO THE DESIRED LENGTH OF COMBINATION

SAT = 7.58 ## CHANGE ME TO THE NUMBER OF SECONDS ONE FULL ATTEMPT TAKES

posCom = [] ## DO NOT CHANGE ME




# Build a set of four, order the set for comparison, check against known list adding if not in


#Citation 1 & 2
for combination in itertools.combinations(set(buttons), comLen):
	if combination not in posCom:
		posCom.append(combination)

print('\n\n********************\n********************\nThere are {combos} possible combinations in scope\n\nAt {perAtt} seconds per attempt, a bruteforce attack could take up to {attackTime:1.1f} minutes to complete.\n\nPlease see below for the ordered list of all combinations\n********************\n********************\n\n'.format(combos=len(posCom),perAtt=SAT, attackTime=(SAT*len(posCom)/60)))

sleep(10)

for com in posCom:
	print(com)
	sleep(0.1)
				
		
