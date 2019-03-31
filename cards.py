from random import shuffle

class Cards():
    def __init__(self):
        cards_list =  []
        for x in ['naghshe','ganj','Jolly Roger','tooti']:
            for i in range(1,14):
                cards_list.append({x:i})
        for x in range(5):
            cards_list.append({"special":'Escape card'})
        for x in range(5):
            cards_list.append({"special":'Pirate'})
        cards_list.append({"special":'Skull King'})
        #cards_list.append({"special":'Tigress'})
        cards_list.append({"special":'Mermaid'})
        cards_list.append({"special":'Mermaid'})
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


