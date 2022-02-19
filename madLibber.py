 #!/bin/python3

import random
from time import sleep


# set globals

story_time = True
verbs_set = False
names_set = False
places_set = False
adverbs_set = False
adjectives_set = False
nouns_set = False
playing = True


# set functions


def rando(a_list):

	rando_list = random.shuffle(a_list)
	return rando_list
	
	
# housekeeping


pretty_banner = ''' 
   _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( m | a | d | L | i | b | b | e | r )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
  
            by 7R!XxSec
  
'''

welcome = "Welcome to MadLibber, keep playing to experience all three possible stories ^_^"


print("\r\n" + pretty_banner + "\r\n" + welcome + "\r\n")
sleep(2)


# Take user input for verbs, names, places, adjectives, adverbs, nouns
# Ask for a comma separated list of verbs
# Split this string at the comma, cut the spaces off, and throw the words into a list
# Doesn't matter the list size
# scramble the lists

while playing == True:


	while verbs_set is False:

    
		verbs = input("\r\n" + "Please enter at least ten verbs in a comma-separated list, such as ... " + "\r\n" + "'train, cut, write, perform, ...'" + "\r\n").split(',')
		verbs = list(verbs)
	
		for item in range(len(verbs)):
			verbs[item] = verbs[item].strip()
	
		
		if len(verbs) >= 10:
        
			print("\r\n" + "Verbs accepted" + "\r\n")
			sleep(1)
			verbs_set = True
		
		else:
	
			print("\r\n" + "Something is wrong with your list, is it long enough?" + "\r\n")

	while names_set is False:

    
		names = input("\r\n" + "Please enter at least ten names in a comma-separated list, such as ... " + "\r\n" + "'John, Matthew, Sherry, Jean, ...'" + "\r\n").split(',')
		names = list(names)
	
		for item in range(len(names)):
			names[item] = names[item].strip()
	
		
		if len(names) >= 10:
        
			print("\r\n" + "Names accepted" + "\r\n")
			sleep(1)
			names_set = True
		
		else:
	
			print("\r\n" + "Something is wrong with your list, is it long enough?" + "\r\n")
		
		
	while places_set is False:

    
		places = input("\r\n" + "Please enter at least ten places in a comma-separated list, such as ... " + "\r\n" + "'London, Canada, Outside, The Ranch, ...'" + "\r\n").split(',')
		places = list(places)
	
		for item in range(len(places)):
			places[item] = places[item].strip()
	
		
		if len(places) >= 10:
        
			print("\r\n" + "Places accepted" + "\r\n")
			sleep(1)
			places_set = True
		
		else:
	
			print("\r\n" + "Something is wrong with your list, is it long enough?" + "\r\n")
		
		
	while adjectives_set is False:

    
		adjectives = input("\r\n" + "Please enter at least ten adjectives in a comma-separated list, such as ... " + "\r\n" + "'flowery, capable, beautiful, tragic, ...'" + "\r\n").split(',')
		adjectives = list(adjectives)
	
		for item in range(len(adjectives)):

			adjectives[item] = adjectives[item].strip()
	
		
		if len(adjectives) >= 10:
        
			print("\r\n" + "Adjectives accepted" + "\r\n")
			sleep(1)
			adjectives_set = True
		
		else:
	
			print("\r\n" + "Something is wrong with your list, is it long enough?" + "\r\n")
		
		
	while adverbs_set is False:

    
		adverbs = input("\r\n" + "Please enter at least ten adverbs in a comma-separated list, such as ... " + "\r\n" + "'quickly, completely, lazily, dumbfoundedly, ...'" + "\r\n").split(',')
		adverbs = list(adverbs)
	
		for item in range(len(adverbs)):

			adverbs[item] = adverbs[item].strip()
	
		
		if len(adverbs) >= 10:
        
			print("\r\n" + "Adverbs accepted" + "\r\n")
			sleep(1)
			adverbs_set = True
		
		else:
	
			print("\r\n" + "Something is wrong with your list, is it long enough?" + "\r\n")
		
	while nouns_set is False:

    
		nouns = input("\r\n" + "Please enter at least ten nouns in a comma-separated list, such as ... " + "\r\n" + "'frog, tree, cloud, apple, ...'" + "\r\n").split(',')
		nouns = list(nouns)
	
		for item in range(len(nouns)):

			nouns[item] = nouns[item].strip()
	
		
		if len(nouns) >= 10:
        
			print("\r\n" + "Nouns accepted" + "\r\n")
			sleep(1)
			nouns_set = True
		
		else:
	
			print("\r\n" + "Something is wrong with your list, is it long enough?" + "\r\n")
		
		

	# Randomize user input

	rando(verbs)
	rando(names)
	rando(places)
	rando(adjectives)
	rando(adverbs)
	rando(nouns)


	# Selection of three one paragraph stories with alienable verbs, names, places, adjectives, adverbs, nouns
	# assign paragraphs to a variable
	# string format the verbs, names, places, adjectives, adverbs, nouns assigning each a value from the scrambled lists
	# make sure that if the original word is used in multiple places that the doctored version receives the same



	story_one = "On a mango tree in a {PLACEONE}, there lived many birds. They were happy in their small nests. Before the onset of the {ADJECTIVEONE} season, all the animals of the {PLACEONE} {VERBONE} their homes. The birds also made their homes more {ADJECTIVETWO}. Many birds brought twigs and leaves and others {VERBTWO}ed their nests. 'We should also store some {NOUNONE}s for our children,' chirped one of the birds. And they collected {NOUNONE}s, until they had enough to see them through the {ADJECTIVEONE} season. They kept themselves busy preparing for the {ADJECTIVETHREE} times. Soon the Storm of {NOUNTWO}s came. It was followed by {NOUNTHREE}s and {NOUNFOUR}s. All the animals and birds stayed in their homes. It continued {VERBONE}ing for many days. One day, {NAMEONE}, wet in the {NOUNTWO}, came into the forest. He sat on a branch, and {VERBTWO}ed. Poor {NAMEONE} tried his best to get shelter, but in vain. The leaves were not enough to save him from the Storm of {NOUNTWO}s. The birds were watching all this. They felt sorry for {NAMEONE} but there was little they could do for him. One of them said, 'Brother! Our small nests are not enough to {VERBTHREE} for you'. Another bird said, 'All of us prepared for the {ADJECTIVEONE} season. If you had, you would not be in this piteous situation'. 'How dare you tell me what to do?' said {NAMEONE}, growling at the bird. {NAMEONE} angrily pounced on the bird’s nest, tore it and threw it on the ground. The bird and her chicks were helpless. The poor bird thought, 'Fools never {VERBFOUR} good advice. It is better not to advise them.'".format(VERBONE = verbs[0] , VERBTWO = verbs[1] , VERBTHREE = verbs[2] , VERBFOUR = verbs[3] , NAMEONE = names[0] , PLACEONE = places[0] , ADJECTIVEONE = adjectives[0] , ADJECTIVETWO = adjectives[1] , ADJECTIVETHREE = adjectives[2] , NOUNONE = nouns[0] , NOUNTWO = nouns[1] , NOUNTHREE = nouns[2] , NOUNFOUR = nouns[3] ) + "\r\n\r\n" + "Credit: http://www.english-for-students.com/Advising-A-Fool.html"


	story_two = "{NAMEONE}, Goddess of {VERBONE} fell in love with a youth named {NAMETWO}, and the two spent many {ADJECTIVEONE} years together. But while {NAMEONE}, being a goddess, retained her youth, {NAMETWO} began to age. He asked his beloved to grant him immortality. She couldn’t do it on her own so she pleaded his case with {NAMETHREE}, the supreme deity. {NAMETHREE} {ADVERBONE} granted the boon. However, {NAMETWO} had forgotten to ask for eternal youth. So though he could not die he could age. As his age advanced he became {ADJECTIVETWO} and {ADJECTIVETHREE} and {ADJECTIVEFOUR}ly ugly. He pleaded with {NAMEONE} to {VERBTWO} him. She could not take back the gift of immortality nor could she give him back his youth. But she could change his form. She turned him into a {NOUNONE}.".format(NOUNONE = nouns[0] , VERBONE = verbs[0] , VERBTWO = verbs[1] , ADJECTIVEONE = adjectives[0] , ADJECTIVETWO = adjectives[1] , ADJECTIVETHREE = adjectives[2] , ADJECTIVEFOUR = adjectives[3] , NAMEONE = names[0] , NAMETWO = names[1] , NAMETHREE = names[2] , ADVERBONE = adverbs[0]) + "\r\n\r\n" +  "Credit: http://www.english-for-students.com/The-Man.html"


	story_three = "{NAMEONE} was an {ADJECTIVEONE} thief. He {VERBONE}ed the rich and gave all to the sick and the needy. The other thieves were jealous of him. They planned to {VERBTWO} him. They challenged him to steal {NAMETWO}'s Pyjamas. {NAMEONE} accepted the challenge. He charted out a plan to steal {NAMETWO}'s pyjamas. He went to {NAMETWO}'s home. He found {NAMETWO} {VERBONE}ing. He opened a bottle of red ants. {NAMETWO} was badly bitten. He cried for help. The servants rushed in. They tried to stop the ants but could not. {NAMEONE} then appeared and offered his help, he instructed {NAMETWO} to remove his pyjamas where the ants were crawling and that {NAMEONE} would take the pyjamas to be washed. Upon returning with {NAMEONE}'s pyjamas, the other thieves were {VERBTHREE}ed dumb.".format(VERBONE = verbs[0] , VERBTWO = verbs[1] , VERBTHREE = verbs[2] , NAMEONE = names[0] , NAMETWO = names[1] , ADJECTIVEONE = adjectives[0] , PLACEONE = places[0]) + "\r\n\r\n" + "Credit: http://www.english-for-students.com/Clever-Thief.html"
		

	# Randomize the story choice and display

	story_book = [story_one, story_two, story_three]
	rando(story_book)

	print("\r\n" + "STORY TIME!" + "\r\n")
	print(story_book[0])
	print("\r\n")

	# Request play again, and if so whether or not to use same words		
		
		
	play_again = list(input("Would you like to play again?" ))

	if str(play_again[0].lower()) == 'y':	
	
		new_words = list(input("Would you like to choose new words?" ))
		
		if str(new_words[0].lower()) == 'y':
		
			verbs_set = False
			names_set = False
			places_set = False
			adverbs_set = False
			adjectives_set = False
			nouns_set = False

	else:
	
		print("\r\n" + "Thank you for playing!" + "\r\n")		
		
		
		
		
