from game import Game
from player import Player
from cards import Cards
from bot_single_commands import *

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
        yuhuha_answer = yuhuhaAskInPV(player, yuhuha_list)
        player._yuhuha = yuhuha_answer
        round_yuhuha.append(yuhuha_answer)
    showInGroup(thisgame,round_yuhuha,"yuhuha")
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
        acceptable_cards = acceptableCards(thisgame,mycards,set_info)
        answer = cardAskInPV(this_player,acceptable_cards)
        card_index = thisgame.player_list[setstarter].mycards.index(answer)
        this_card = thisgame.player_list[setstarter].mycards.pop(card_index)
        print("chosed card",this_card)
        #addToTable(this_player,this_card,thisgame)
        set_info.append({this_player.name:this_card})
        showInGroup(thisgame, set_info,"set info")
        setstarter +=1
        setstarter = setstarter % len(thisgame.player_list)
    setwinner = judgment_set(set_info,thisgame)
    print("winner",thisgame.player_list[setwinner].name)
    return setwinner

def scoreupdate(thisgame):
    score = []
    for player in thisgame.player_list:
        score.append({player.name:player.totalscore})
    print("score",score)
    showInGroup(thisgame, score,"score")


def acceptableCards(thisgame, mycards,set_info):

    print("acceptableCards")
    print(set_info)
    newcards = []

    hokm = None
    hokm_darim = False

    if len(set_info) > 0 :
        for c in set_info:

            player_name = list(c)[0]
            card_ = c[player_name]
            cardtype = list(card_)[0]
            cardvariation = card_[cardtype]

            if cardtype is not "special":
                hokm = cardtype
                break

    if hokm is not None:
        for card in mycards:
            if list(card)[0] is hokm:
                hokm_darim = True


    for card in mycards:
        if hokm is None:
            pass

        print(".")
        if hokm is None:
            newcards.append(card)
            print(1)
        elif hokm_darim is False:
            newcards.append(card)
            print(1.1)
        else :
            if list(card)[0] is "special":
                newcards.append(card)
                print(2)
            elif list(card)[0] is hokm:
                newcards.append(card)
                print(3)

    print("hokm",hokm)
    print("hokm_darim",hokm_darim)
    return newcards

def addToTable(player,card,thisgame):
    thisgame.cards_on_table.append({player:card})
    showInGroup(thisgame, thisgame.cards_on_table,"cards on board")
    pass



def judgment_set(set_info,thisgame):
    #essencial player_card s
    print("set info again")
    print(set_info)
    bestcard = None
    bestcard_type = None
    bestcard_vari = None
    hokm = None
    firstmemaid = None
    skullking = None

    for player_card in set_info:
        print(player_card)
        print(bestcard)
        player_name = list(player_card)[0]
        card = player_card[player_name]
        cardtype = list(card)[0]
        cardvariation = card[cardtype]

        if bestcard == None:
            print("initial")
            bestcard = player_card
            bestcard_type = list(bestcard[list(bestcard)[0]])[0]
            bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
            if cardtype is not "special":
                hokm = cardtype
            continue


        if hokm == None:
            print("set hokm")
            if cardtype is not "special":
                hokm = cardtype

        if cardtype == "special":
            print("special card")
            #Mermaid
            if cardvariation == "Mermaid":
                print("Mermaid")
                if firstmemaid is None:
                    firstmemaid = player_card
                if bestcard_type == "special":
                    if bestcard_vari is not 'Escape card':
                        continue
                else:
                    bestcard = player_card
                    bestcard_type = list(bestcard[list(bestcard)[0]])[0]
                    bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
                    continue

            #skull king
            if cardvariation == "Skull King":
                print("skull")
                skullking = player_card
                bestcard = player_card
                bestcard_type = list(bestcard[list(bestcard)[0]])[0]
                bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
                continue

            #Pirate
            if cardvariation == "Pirate":
                print("pirate")
                if bestcard_vari is not "Skull King":
                    bestcard = player_card
                    bestcard_type = list(bestcard[list(bestcard)[0]])[0]
                    bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
                    continue

        #not spcecial
        else:
            print("not special")
            if cardtype is hokm:
                if bestcard_type is not hokm :#or bestcard_type is "Jolly Roger" or bestcard_type is "special": # type check of bestcard
                    print("hokm but not working")
                    pass
                elif cardvariation > bestcard_vari: # variarion check of bestcard
                    print("hokm with more value")
                    bestcard = player_card
                    bestcard_type = list(bestcard[list(bestcard)[0]])[0]
                    bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
                    continue
            elif cardtype == "Jolly Roger" :
                print("jolly ")
                if bestcard_type is not "special" or bestcard_vari is not "Escape card":
                    print("jolly win")
                    bestcard = player_card
                    bestcard_type = list(bestcard[list(bestcard)[0]])[0]
                    bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]


    if skullking is not None and firstmemaid is not None:
        bestcard = firstmemaid

    winner = 0  # winner is the index of won player in player_list

    player_name = list(bestcard)[0]
    for i in range(len(thisgame.player_list)):
        if player_name == thisgame.player_list[i].name:
            winner = i

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
