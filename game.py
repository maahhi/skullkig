from player import Player
from cards import Cards
class Game():
    def __init__(self,id):
        self.game_id = id
        self.player_list=[]
        self.cards = Cards
        self.score_board = {} # {player:score}
        self.cards_on_table = [] # [{player:card}]


    def add_player(self,player):
        self.player_list.append(player)
        self.score_board.add({player:0})

    def dast_dadan_dar_yek_round(self):
        pass

    def round_up(self):
        self.first_player=self.player_list[self.round % self.player_count ]

        for player in self.player_list:
            Cards.dast_bede(self.round)

        for i in range(self.round):
            self.set_up()

        self.round += 1
        #end of round

    def set_up(self):
        cards_in_this_set=[]






