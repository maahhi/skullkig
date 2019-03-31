from game import Game
from player import Player
from cards import Cards

#yeki too grouh darkhaste sakhte bazi bede
def create_newgame(gameid,group_name):
    newgame = Game(gameid,group_name)
    return newgame


#adam ha be bazi ezafe beshan
def create_newplayer_for_thisgame(playerNAME,playerid,thisgame):
    newplayer = Player(playerNAME,playerid)
    thisgame.add_player(newplayer)


#bazi shooroo beshe
def starting_game(thisgame):
    scoreupdate(thisgame)
    for i in range(1,11):
        newround(i,thisgame)


def newround(round_number,thisgame):
    thisgame.cards = Cards()
    round_yuhuha =  []
    round_info = [] # player:winsets
    for player in thisgame.player_list:
        round_info.append(0)

    for player in thisgame.player_list:
        dast = thisgame.cards.dast_bede(round_number)
        player.mycards=dast
        showInPV( player,dast)

    for player in thisgame.player_list:
        yuhuha = min(round_number,5)
        yuhuha_list = [i for i in range(0,yuhuha+1)]
        yuhuha_answer = askInPV(player,yuhuha_list)
        player._yuhuha = yuhuha_answer
        round_yuhuha.append(yuhuha_answer)

    setstarter = (round_number-1) % len(thisgame.player_list)
    for i in range(round_number):
        print("new set +++++")
        setstarter = newset(setstarter,thisgame)
        round_info[setstarter]+=1
    judgment_round(round_number,round_info,round_yuhuha,thisgame)
    scoreupdate(thisgame)

def newset(setstarter, thisgame):
    print("set starter index:",setstarter)
    set_info = [] # player_name:card
    for i in range(len(thisgame.player_list)):
        this_player = thisgame.player_list[setstarter]
        mycards = this_player.mycards
        acceptable_cards = acceptableCards(thisgame,mycards)
        answer = askInPV(this_player,acceptable_cards)
        card_index = thisgame.player_list[setstarter].mycards.index(answer)
        this_card = thisgame.player_list[setstarter].mycards.pop(card_index)
        print("chosed card",this_card)
        #addToTable(this_player,this_card,thisgame)
        set_info.append({this_player.name:this_card})
        showInGroup(set_info,"set info")
        setstarter +=1
        setstarter = setstarter % len(thisgame.player_list)
    setwinner = judgment_set(set_info)
    print("winner",thisgame.player_list[setwinner].name)
    return setwinner

def scoreupdate(thisgame):
    score = []
    for player in thisgame.player_list:
        score.append({player.name:player.totalscore})
    print("score",score)
    showInGroup(score,"score")

def showInPV(player,dast):
    print("show in pv")
    print(player.name)
    print(dast)
    pass

def askInPV(player,choise):#it should return the object
    print("ask in pv")
    answer = 0
    print(choise)
    answer = int(input(player.name))
    return choise[answer]

def acceptableCards(thisgame, mycards):
    return mycards

def addToTable(player,card,thisgame):
    thisgame.cards_on_table.append({player:card})
    showInGroup(thisgame.cards_on_table,description="cards on board")
    pass

def showInGroup(input,description):
    print("show in group")
    print(description)
    for i in input:
        print(i)
    pass

def judgment_set(set_info):
    winner = 1 # winner is the index of won player in player_list
    return winner

def judgment_round(round_number,round_info,round_yuhuha,thisgame):
    for i in range(len(thisgame.player_list)):
        if round_yuhuha[i] == 0 :
            if round_info[i] == 0:
                thisgame.player_list[i].totalscore += 10 * round_number
            else:
                thisgame.player_list[i].totalscore -= 10 * round_number
        else:
            if round_yuhuha[i]==round_info[i]:
                thisgame.player_list[i].totalscore += 20 * round_info[i]
            else:
                thisgame.player_list[i].totalscore -= 10 * abs(round_info[i] - round_yuhuha[i])
