# useful objects for dnd reference




class dnd_character:
    # init 
    def __init__(self, player_name=None, config=None):
        # check for player_name, if not provided, throw error
        if player_name == None:
            raise ValueError('player_name not provided')
        else:
            self.player_name = player_name
        # check config/preset.json for player_name
            

    # methods    
    def update_party(self, party_name):
        pass

    def level_up(self, dnd_class):
        pass 

    










class dnd_Party:

    def __init__(self, founder_name, party_name, member_names):
        self.founder_name = founder_name
        self.party_name = party_name
        self.member_names = member_names
