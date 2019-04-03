from game import Game
from player import Player
from cards import Cards
from bot_single_commands import *

from card_emojies import *

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
    thisgame.gamestat = 1
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
    yuhuha_showingp = []
    for player in thisgame.player_list:
        name = player.name
        yuhuha = min(round_number,5)
        yuhuha_list = [i for i in range(0,yuhuha+1)]
        yuhuha_answer = (yuhuhaAskInPV(player, yuhuha_list))[1]
        player._yuhuha = yuhuha_answer
        round_yuhuha.append(yuhuha_answer)
        yuhuha_showingp.append({name:yuhuha_answer})

    showInGroup(thisgame,yuhuha_showingp,"yuhuha")
    setstarter = (round_number-1) % len(thisgame.player_list)
    for i in range(round_number):
        #print("new set +++++")
        setstarter = newset(setstarter,thisgame)
        showInGroup(thisgame,thisgame.player_list[setstarter].name,"winner")
        round_info[setstarter]+=1
    judgment_round(round_number,round_info,round_yuhuha,thisgame)
    scoreupdate(thisgame)

def newset(setstarter, thisgame):
    #print("set starter index:",setstarter)
    set_info = [] # player_name:card
    for i in range(len(thisgame.player_list)):
        this_player = thisgame.player_list[setstarter]
        mycards = this_player.mycards
        acceptable_cards = acceptableCards(thisgame,mycards,set_info)
        answer = cardAskInPV(this_player,acceptable_cards)
        card_index = thisgame.player_list[setstarter].mycards.index(answer)
        this_card = thisgame.player_list[setstarter].mycards.pop(card_index)
        #print("chosed card",this_card)
        #addToTable(this_player,this_card,thisgame)
        set_info.append({this_player.name:this_card})
        showInGroup(thisgame, set_info,"cards on board")
        setstarter +=1
        setstarter = setstarter % len(thisgame.player_list)
    setwinner = judgment_set(set_info,thisgame)
    #print("winner",thisgame.player_list[setwinner].name)
    return setwinner

def scoreupdate(thisgame):
    score = []
    for player in thisgame.player_list:
        score.append({player.name:player.totalscore})
    #print("score",score)
    showInGroup(thisgame, score,"score")


def acceptableCards(thisgame, mycards,set_info):

    #print("acceptableCards")
    #print(set_info)
    newcards = []

    hokm = None
    hokm_darim = False

    if len(set_info) > 0 :
        for c in set_info:

            player_name = list(c)[0]
            card_ = c[player_name]
            cardtype = list(card_)[0]
            cardvariation = card_[cardtype]

            if cardtype != "special":
                hokm = cardtype
                break

    if hokm == None:
        for card in mycards:
            if list(card)[0] == hokm:
                hokm_darim = True


    for card in mycards:
        if hokm == None:
            pass

        #print(".")
        if hokm == None:
            newcards.append(card)
            #print(1)
        elif hokm_darim == False:
            newcards.append(card)
            #print(1.1)
        else :
            if list(card)[0] == "special":
                newcards.append(card)
                #print(2)
            elif list(card)[0] == hokm:
                newcards.append(card)
                #print(3)

    #print("hokm",hokm)
    #print("hokm_darim",hokm_darim)
    return newcards

def addToTable(player,card,thisgame):
    thisgame.cards_on_table.append({player:card})
    showInGroup(thisgame, thisgame.cards_on_table,"cards on board")
    pass



def judgment_set(set_info, thisgame):
    #essencial player_card s
    #print("set info again")
    #print(set_info)
    bestcard = None
    bestcard_type = None
    bestcard_vari = None
    hokm = None
    firstmemaid = None
    skullking = None

    for player_card in set_info:
        print(player_card)

        player_name = list(player_card)[0]
        card = player_card[player_name]
        cardtype = list(card)[0]
        cardvariation = card[cardtype]

        if bestcard == None or bestcard_vari == 'Escape'+e_Escape :
            if cardvariation == 'Escape'+e_Escape and bestcard_vari == 'Escape'+e_Escape:
                continue
            print("initial")
            bestcard = player_card
            bestcard_type = list(bestcard[list(bestcard)[0]])[0]
            bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
            if cardtype != "special":
                print("set hokm")
                hokm = cardtype
            continue


        if hokm == None:
            if cardtype != "special":
                print("set hokm")
                hokm = cardtype
                continue

        if cardtype == "special":
            print("special card")

            # skull king
            if cardvariation == "Skull King" + e_Skull_King:
                print("skull")
                skullking = player_card
                bestcard = player_card
                bestcard_type = list(bestcard[list(bestcard)[0]])[0]
                bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
                continue

            # Pirate
            if cardvariation == "Pirate" + e_Pirate:
                print("in pirate")
                if bestcard_vari != "Skull King" + e_Skull_King:
                    if bestcard_vari != "Pirate" + e_Pirate:
                        print("set pirate")
                        print(bestcard)
                        print(player_card)
                        bestcard = player_card
                        bestcard_type = list(bestcard[list(bestcard)[0]])[0]
                        bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
                        continue

            #Mermaid
            if cardvariation == "Mermaid"+e_Mermaid:
                print("Mermaid")
                if firstmemaid == None:
                    firstmemaid = player_card
                    if bestcard_vari != "Skull King" + e_Skull_King:
                        if bestcard_vari != "Pirate" + e_Pirate:
                            bestcard = player_card
                            bestcard_type = list(bestcard[list(bestcard)[0]])[0]
                            bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
                            continue

        # not spcecial
        else:
            # jolly
            if cardtype == "Jolly Roger"+e_Jolly_Roger :
                print("jolly ")
                if bestcard_type == "special":
                    if bestcard_vari ==  "Skull King" + e_Skull_King or bestcard_vari == "Pirate" + e_Pirate or bestcard_vari == "Mermaid"+e_Mermaid :
                        continue
                if bestcard_type == "Jolly Roger"+e_Jolly_Roger and bestcard_vari > cardvariation:
                    continue
                bestcard = player_card
                bestcard_type = list(bestcard[list(bestcard)[0]])[0]
                bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
                continue

            # hokm
            if cardtype != hokm:
                if bestcard_type == "special":
                    if bestcard_vari ==  "Skull King" + e_Skull_King or bestcard_vari == "Pirate" + e_Pirate or bestcard_vari == "Mermaid"+e_Mermaid :
                        continue
                if bestcard_type == "Jolly Roger" + e_Jolly_Roger :
                    continue
                if bestcard_type == hokm and bestcard_vari > cardvariation:
                    continue
                bestcard = player_card
                bestcard_type = list(bestcard[list(bestcard)[0]])[0]
                bestcard_vari = bestcard[player_name][list(bestcard[list(bestcard)[0]])[0]]
                continue



    if skullking != None and firstmemaid != None:
        bestcard = firstmemaid

    winner = 0  # winner is the index of won player in player_list

    player_name = list(bestcard)[0]
    for i in range(len(thisgame.player_list)):
        if player_name == thisgame.player_list[i].name:
            winner = i
    print("bestcard : ", bestcard)
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
