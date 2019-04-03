from random import shuffle

from card_emojies import *


class Cards():
    def __init__(self):
        cards_list =  []
        for x in ['naghshe'+e_naghshe,'ganj'+e_ganj,'Jolly Roger'+e_Jolly_Roger,'tooti'+e_tooti]:
            for i in range(1,14):
                cards_list.append({x:i})
        for x in range(5):
            cards_list.append({"special":'Escape'+e_Escape})
        for x in range(5):
            cards_list.append({"special":'Pirate'+e_Pirate})
        cards_list.append({"special":'Skull King'+e_Skull_King})
        #cards_list.append({"special":'Tigress'})
        cards_list.append({"special":'Mermaid'+e_Mermaid})
        cards_list.append({"special":'Mermaid'+e_Mermaid})
        self.cards_list = cards_list
        shuffle(self.cards_list)
        #print(self.cards_list)

    def shuffle(self):
        print("shuffling")
        shuffle(self.cards_list)
        print(self.cards_list)

    def dast_bede(self,chandta):
        dast=[]
        for i in range(chandta):
            dast.append(self.cards_list.pop())
        #print(dast)
        return dast


