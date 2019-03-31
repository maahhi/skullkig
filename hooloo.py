from cards import Cards
from game import Game
from player import Player

import senario
thisgame=senario.create_newgame(0)
senario.create_newplayer_for_thisgame("mahya",thisgame)
senario.create_newplayer_for_thisgame("ali",thisgame)
senario.create_newplayer_for_thisgame("ehsan",thisgame)
senario.scoreupdate(thisgame)