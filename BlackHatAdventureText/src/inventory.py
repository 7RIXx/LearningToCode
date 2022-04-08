from src.database.items import items

class ItemShop:
    def __init__(self):
        """
        """
        self.items = {}
 
    def show_store_inventory(self):
        """
        prints the store inventory
        """
        #dict.copy() makes a "shallow" copy of the dict, allowing you to itterate over the 
        # dict without manipulating the original dict
        for item in self.items.copy():
            # this is an example of string formatting a block quote
            # the f goes in front of the string and it allows you to 
            # format entities into the brackets by name
            thing_to_print = f'''{item} : {self.items.get(item)}'''
            print(thing_to_print)
    
    # an example of explicitly specifying the entity type being returned from this function
    def validate_inventory_choice_by_id(self,item_id) -> bool:
        """
        makes sure they chose an item in the list and 
        are not throwing random garbage into the terminal
        """
        # validation is a good idea, good job!
        try:
            self.items.get(item_id)
            return True
        except:
            print("Rogue packets detected, the authorities have been alerted to this IP, please remain where you are.")
            return False
    
    # now you try!
    def validate_inventory_choice_by_name(self,item_name)-> bool:
        """
        Validates an inventory selection by using the name instead of a number
        """
        try:
            #self.items.get(item_name)  #this method only grabs on the key, so...
            if item_name in self.items:
                return true
       except:
            print("Rogue packets detected, the authorities have been alerted to this IP")
            return False

    def ask_for_choice(self) -> int:
        #choice = input("I choose:")
        #return choice
        return input("I choose: ")

    def set_personal_inventory(self):
        """
        returns a dict of items chosen by the player
        used for assigning the items at start of game
        or when visiting a shop
        """
        personal_inventory = {}
        print('''
        
        Please choose four items from this list, to take with you on your journey
        enter the number assigned to that item.
        
        ''')
        self.show_store_inventory()
        while len(personal_inventory) < 4:
            new_item_id = self.ask_for_choice()
            # now we check if they chose an item in the store
            if self.validate_inventory_choice_by_id(new_item_id):
                personal_inventory.update({new_item_id : self.items.get(new_item_id)})
        return personal_inventory

    def additemtogame(self,item:dict):
        """
        adds items to game database
        
        Should be passed as arg into player_object creation?
        """
        return item

# testing the code, this should be done in a unit test file, separate freom the main code
# if you run this file in the terminal by itself with 
# python3 inventory.py
# it will run the following code
if __name__ == "__main__":
    new_item_store = ItemShop()
    new_player_inventory = new_item_store.set_personal_inventory()
    print(new_player_inventory)
