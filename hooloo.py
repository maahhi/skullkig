
import senario
thisgame=senario.create_newgame(0,"var ha")
senario.create_newplayer_for_thisgame("mahya",111,thisgame)
senario.create_newplayer_for_thisgame("ali",222,thisgame)
senario.create_newplayer_for_thisgame("ehsan",333,thisgame)
senario.scoreupdate(thisgame)

senario.newround(3,thisgame)