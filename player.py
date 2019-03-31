class Player():
    def __init__(self,player_name,id):
        self.name = player_name
        self.id = id
        self._yuhuha = 0
        self.mycards = []
        self.totalscore = 0
        pass

    def yuhuha(self,adad):
        self._yuhuha = adad

    def send_me_cards(self,cards):
        print(cards)


