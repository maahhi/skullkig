import pytest

from card_emojies import *

from game import Game
from player import Player
from senario import judgment_set


@pytest.fixture(scope="module")
def game():
    game_instance = Game(0, 0)
    game_instance.player_list = [
        Player('Player0', 0),
        Player('Player1', 1),
        Player('Player2', 2),
        Player('Player3', 3)
    ]
    return game_instance


def test_judgment_set_simple_00(game):
    simpleCard = 'naghshe'+e_naghshe
    info = [
        {'Player0': {simpleCard: 13}},
        {'Player1': {simpleCard: 8}},
        {'Player2': {simpleCard: 5}},
        {'Player3': {simpleCard: 1}}
    ]

    for _ in range(4):
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 0


def test_judgment_set_simple_01(game):
    simpleCard1 = 'naghshe' + e_naghshe
    simpleCard2 = 'ganj'+e_ganj
    info = [
        {'Player0': {simpleCard1: 13}},
        {'Player1': {simpleCard2: 8}},
        {'Player2': {simpleCard1: 5}},
        {'Player3': {simpleCard2: 1}}
    ]

    for _ in range(2):
        info.insert(0, info.pop())
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 0
    info.insert(0, info.pop())
    for _ in range(2):
        info.insert(0, info.pop())
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 1


def test_judgment_set_simple_02(game):
    simpleCard1 = 'naghshe' + e_naghshe
    simpleCard2 = 'ganj' + e_ganj
    simpleCard3 = 'tooti'+e_tooti
    info = [
        {'Player0': {simpleCard1: 13}},
        {'Player1': {simpleCard2: 12}},
        {'Player2': {simpleCard3: 11}}
    ]

    for i in range(2):
        print(i)
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 2-i

