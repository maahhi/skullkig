from game import Game
from player import Player
from cards import Cards

#yeki too grouh darkhaste sakhte bazi bede
def create_newgame(gameid):
    newgame = Game(gameid)
    return newgame


#adam ha be bazi ezafe beshan
def create_newplayer_for_thisgame(playerIDorNAME,thisgame):
    newplayer = Player(playerIDorNAME)
    thisgame.add_player(newplayer)


#bazi shooroo beshe
def starting_game(thisgame):
    scoreupdate()
    for i in range(1,11):
        newround(i,thisgame)


def newround(round_number,thisgame):
    thisgame.cards = Cards
    round_yuhuha =  []
    round_info = {} # player:winsets
    for player in thisgame.player_list:
        round_info.update({player:0})

    for player in thisgame.player_list:
        dast = thisgame.cards.dast_bede(round_number)
        player.mycards=dast
        showInPV(dast, player)

    for player in thisgame.player_list:
        yuhuha = min(round_number,5)
        yuhuha_list = [i for i in range(0,yuhuha+1)]
        yuhuha_answer = askInPV(yuhuha_list)
        player._yuhuha = yuhuha_answer
        round_yuhuha.append(yuhuha_answer)

    setstarter = round_number % len(thisgame.player_list)
    for i in range(round_number):
        setstarter = newset(setstarter,thisgame)
        round_info[setstarter]+=1
    judgment_round(round_info,round_yuhuha,thisgame)
    scoreupdate()

def newset(setstarter, thisgame):
    set_info = [] # player:card
    for i in range(len(thisgame.player_list)):
        this_player = thisgame.player_list[setstarter]
        mycards = this_player.mycards
        acceptable_cards = acceptableCards(thisgame,mycards)
        answer = askInPV(acceptable_cards,this_player)
        card_index = thisgame.player_list[setstarter].mycards.index(answer)
        this_card = thisgame.player_list[setstarter].mycards.pop(card_index)
        addToTable(this_player,this_card,thisgame)
        set_info.append({this_player:this_card})
        showInGroup(set_info)
        setstarter +=1
        setstarter = setstarter % len(thisgame.player_list)
    setwinner = judgment_set(set_info)
    return setwinner

def scoreupdate(thisgame):
    score={}
    for el in thisgame.score_board:
        score.update({el.name:thisgame.score_board[el]})
    print(score)
    showInGroup(score,"score")

def showInPV(dast, player):
    pass

def askInPV(choise, player):
    answer = 1
    return answer

def acceptableCards(thisgame, mycards):
    return mycards

def addToTable(player,card,thisgame):
    pass

def showInGroup(input,description):
    pass

def judgment_set(set_info):
    winner = 1
    return winner

def judgment_round(round_info,round_yuhuha,thisgame):
    pass