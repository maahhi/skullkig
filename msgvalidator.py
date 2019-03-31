from gamelist import game_list

def game_found(iden, gl):
    print(gl)
    for g in gl:
        if g.game_id == iden:
            return g
            break
    return False


def is_member_of_the_game(player_id, game):
    for p in game.player_list:
        if p.id == player_id:
            return True
            break
    return False

def is_valid_create_request(msg):
    if msg["chat"]["type"] == "group" and msg["text"][:12] == "/create_game":
        if not game_found(msg["chat"]["id"], game_list):
            return True
        else:
            print("code comes here!")
            return False
    else:
        return False

def is_valid_join_request(msg):
    if msg["chat"]["type"] == "private" and msg["text"][0:6] == "/start":
        if not is_member_of_the_game(msg["chat"]["id"],game_found(int(msg["text"].split()[1]) ,game_list)):
            return True
        else: return False
    else:
        return False

def is_valid_start_game(msg):
    if msg["chat"]["type"] == "group" and msg["text"][:11] == "/start_game":
        if game_found(msg["chat"]["id"], game_list):
            return True
        else:
            print("code comes here!")
            return False
    else:
        return False