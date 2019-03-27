from player import Player
from cards import Cards
class Game():
    def __init__(self,id):
        self.game_id = id
        self.player_list=[]
        self.round = 0
        self.cards = Cards


    def add_player(self,player):
        self.player_list.append(player)

    def strat(self):
        self.first_player = self.player_list[0]
        self.player_count = len(self.player_list)

    def round_up(self):
        self.first_player=self.player_list[self.round % self.player_count ]
        Cards.__init__()
        for player in self.player_list:
            Cards.dast_bede(self.round)

        for i in range(self.round):
            self.set_up()

        self.round += 1
        #end of round

    def set_up(self):
        cards_in_this_set=[]






