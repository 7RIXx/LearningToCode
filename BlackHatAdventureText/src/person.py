class Person:
    def __init__(self):
        """
        Base class representing a player
        Everything in this class is created when you create a player
        using
        >>> newplayer = Player()
        >>> Player.setname("moop mc meeperson)
        """
        self.name = str

        self.inventory = {
            "items"  :[]
            }

    def setname(self,name):
        """
        sets name of player
        example:
            newplayer = Person()
            newplayer.setname("meepers mcgee")
        """
        self.name = name
        
    def set_god_mode(self):
        """
        sets god mode, altering inventory and stats
        """
        # GOD MODE, FOR TESTING THE DECISION TREE
        hacked_inventory = ['badge cloner','blanket','lockpicks','rope','raspberry pi', 'rubber ducky']
        self.inventory["items"] = hacked_inventory




if __name__ == '__main__':

	test = Person()
	
	test.set_god_mode()
	
	print(test.inventory)
