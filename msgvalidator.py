from gamelist import game_list

def game_found(iden, gl):
    print(gl)
    for g in gl:
        if g.game_id == iden:
            return g
            break
    return False


def is_valid_create_request(msg):
    if msg["chat"]["type"] == "group" and msg["text"] == "/newgame@skull_test_bot":
        if not game_found(msg["chat"]["id"], game_list):
            return True
        else:
            print("code comes here!")
            return False
    else:
        return False

def is_valid_join_request(msg):
    print (game_found(int(msg["text"].split()[1]), game_list).player_list)
    if msg["chat"]["type"] == "private" and msg["text"][0:6] == "/start":
        return True
    else:
        return False
