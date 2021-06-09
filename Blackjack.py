#!/bin/python3


'''
ERRORS TO BE FIXED:
    Thing is crawling with bugs, mostly they appear to be coming out of the main logic loop

    A player bust will allow for another hit before breaking

    One time (not every time though) when responding yes to a hit request it just ignored me and moved on to the dealer

    If player busts out then the report of dealer_sum reports they beat you with a sum of zero

'''

from random import shuffle
from time import sleep

# SET GLOBALS

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
dealer_sum = 0
player_sum = 0
stood = False


# BUILD OBJECTS

class Player:

    def __init__(self):
        self.bank = 100
        self.hand = []
        self.pot = 0
        self.bet = 0
        self.name = input("\nTHE MAGICAL CASINO\nPlease tell us your name: ")
        print(f"\nWelcome to the casino, {self.name}")

    def __str__(self):
        return f"\nPlayer: {self.name} \nBank Account: {self.bank:,} ETH"

    def hit(self):
        # Take one card from the top of the deck and add it to the player's hand
        # If not hit, then stand
        self.hand.append(card_deck.get_card())

    def wager(self):
        # Check that the bet does not exceed self.bank
        # Remove the bet from self.bank and add it to self.pot

        while True:
            try:
                self.bet = int(input("\nPlease place a wager: "))
                if self.bet <= self.bank:
                    if self.bet > 0:
                        self.bank -= self.bet
                        self.pot += self.bet
                        break
            except TypeError:
                print(f"{the_player.name}'s Bank: " + str(self.bank) + " ETH")
                print("\r\n" * 2)

    def add_to_hand(self, card):
        card = card
        self.hand.append(card)
        
    def show_hand(self):
        print(f"\n\n{self.name}'s Hand: \n{self.hand}\n")


class Dealer:

    def __init__(self):
        self.hand = []
        self.name = "Dealer"

    def __str__(self):
        return f"a stone-faced and suspiciously witty Blackjack dealer who will now take all your monies"

    def hit(self):
        # Take one card from the top of the deck and add it to the player's hand
        # If not hit, then stand
        self.hand.append(card_deck.get_card())

    def add_to_hand(self, card):
        self.card = card
        self.hand.append(self.card)
        
    def show_hand(self):
        print(f"\n\nDealer's Hand: \n{self.hand}\n")
        
    def show_hand_hidden(self):
        print(f"\n\nDealer's Hand: \n{self.hand[0:-1]},[X]\n")


class Deck:

    def __init__(self):
        self.deck = []
        self.deck.extend(values)
        self.deck.extend(values)
        self.deck.extend(values)
        self.deck.extend(values)

    def __str__(self):
        return "\nDeck currently contains " + str(len(self.deck)) + " cards"

    def __index__(self):
        return "\nDeck: " + str(self.deck)

    def get_card(self):
        # Take the top card in the deck, pop it out, and send it to a player's hand
        card_in_question = self.deck.pop(0)
        return card_in_question

    def shuffle_deck(self):
        # Shuffle deck
        shuffle(self.deck)


class Table:

    def __init__(self):
        pass

    def check_cards(self, someone):  # Pass in the player object
        # A method which will take in a player's hand and check it for win
        # Perhaps this will also contain the logic which can deal with aces
        # This will only return a sum; the actual comparison for win will be in main loop
        hand_to_check = someone.hand
        name_of_player = someone.name
        size_of_hand = len(hand_to_check)
        # We want to take in the hand -- a list --
        # For loop adds each element to a sum and IF the element is an ace increases another counter
        # The sum is checked, if it exceeds 21 AND ace count is > 0 then minus and check again
        hand_sum = 0
        ace_count = 0
        for card in range(size_of_hand):
            if hand_to_check[card] == 11:
                ace_count += 1
                hand_sum += hand_to_check[card]
                continue
            else:
                hand_sum += hand_to_check[card]

        while (hand_sum > 21) and (ace_count > 0):
            hand_sum -= 10
            ace_count -= 1

        return hand_sum


# SET UP THE GAME
# Manifest the Objects for Realz
the_player = Player()
the_dealer = Dealer()
table = Table()
card_deck = Deck()
card_deck.shuffle_deck()

# Have some fun
sleep(2)
print("\nManifesting an exotic dancer for you to play with...")
sleep(5)
print("Hmmm..")
sleep(5)
print("That didn't go quite as planned...")
sleep(5)
print("\nManifested " + str(the_dealer))
sleep(5)
print("\nManifesting a deck of cards...")
print("Shuffling that deck...")
sleep(2)
print("\nHere we go, good luck!")
print("And my honest apologies about the mixup..")
sleep(10)
print("\r\n" * 100)




# MAIN LOGIC LOOP

while the_player.bank > 0:
    try:
        # Clear screen
        print("\r\n" * 100)
        # Deal the dealer two cards
        the_dealer.hit()
        the_dealer.hit()
        # Show one of the dealer's cards
        the_dealer.show_hand_hidden()
        # Deal the player two cards
        the_player.hit()
        the_player.hit()
        print("\r\n" * 3)
        # Show the player's cards
        the_player.show_hand()
        print("\r\n" * 10)
        # Request a wager
        print(f"{the_player.name}'s Bank: " + str(the_player.bank) + " ETH")
        the_player.wager()
        sleep(3)
        print("\r\n" * 100)

        # While not (stood) or (player_sum > 21) continue to request confirmation to hit
        while not stood or player_sum > 21:
            # Each hit, clear screen and post one dealer card and all player cards
            # Also store sum in a variable
            # While hitorstay not in list[n,y,no,yes,No,Yes,NO,YES,N,Y] request input
            answer_list = ["n","y","no","yes","No","Yes","NO","YES","N","Y"]
            yes_list = ["y","yes","Yes","YES","Y"]
            no_list = ["n","no","No","NO","N"]
            hit_or_stay = "temp"
            while not hit_or_stay in answer_list:
                try:
                    the_dealer.show_hand_hidden()
                    the_player.show_hand()
                    hit_or_stay = input("Would you like to hit that? ")
                    print("\r\n" * 100)

                except:
                    print("Invalid response, please try again\n")

            if hit_or_stay in yes_list and not player_sum > 21:
                sleep(2)
                the_player.hit()
                player_sum = table.check_cards(the_player)
            elif hit_or_stay in no_list or player_sum > 21:
                # Clear screen
                print("\r\n" * 100)
                player_sum = table.check_cards(the_player)
                stood = True
                break

        # Dealer's turn to play
        # While not (dealer_sum > player_sum) or (dealer_sum > 21) continue to hit dealer
        target = 0
        if player_sum <= 21:
            target = player_sum
        else:
            target = 21

        while dealer_sum < target:
                if player_sum > 21:
                    break
                else:
                    the_dealer.hit()
                    dealer_sum = table.check_cards(the_dealer)
                    sleep(2)
                    print("\r\n" * 100)
                    the_dealer.show_hand()


        # Compare dealer_sum and player_sum
        # If (player_sum <= 21) and (player_sum > dealer_sum) then
        # Clear screen
        print("\r\n" * 100)
        the_dealer.show_hand()
        print("\r\n" * 3)
        the_player.show_hand()
        if (player_sum <= 21) and ((player_sum > dealer_sum) or (dealer_sum > 21)):
            # PLAYER WINS
            print(f"\n\n{the_player.name} wins double their wager!\n\n")
            print(f"You played {player_sum} against Dealer's {dealer_sum}\n")
            the_player.bank += (the_player.pot * 2)
            the_player.pot = 0
            print(f"{the_player.name}'s Bank Account: ${the_player.bank} ETH\n")
        # elif (player_sum > 21) and (dealer_sum > 21):
        elif (player_sum > 21) and (dealer_sum > 21):
            # BOTH BUST
            print(f"\n\nThis round is a tie, {the_player.name}'s wager is returned to them\n\n")
            print(f"Dealer busted with {dealer_sum}; you busted with {player_sum}\n")
            the_player.bank += the_player.pot
            the_player.pot = 0
            print(f"{the_player.name}'s Bank Account: ${the_player.bank}\n")
        # else player.pot = 0 and continue
        else:
            # DEALER WINS
            print(f"\n\nThe Dealer just took you for your {the_player.pot} ETH\n\n")
            print(f"Dealer played {dealer_sum} against your {player_sum}\n")
            the_player.pot = 0
            print(f"{the_player.name}'s Bank Account: ${the_player.bank}\n")

        sleep(10)

        # Reset for next hand
        the_player.hand = []
        the_dealer.hand = []
        stood = False

        # Test for failure
        if the_player.bank <= 0:
            print("\n\nTold you he'd take all your monies...\n\nHave a nice life.\n\n")
            break

    except KeyboardInterrupt:
        print(f"\n\n{the_player.name}, leaving his ETH on the table, turns and flees from the Magical Casino!\n\n ")
        exit()