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
    simple_card = 'naghshe' + e_naghshe
    info = [
        {'Player0': {simple_card: 13}},
        {'Player1': {simple_card: 1}},
        {'Player2': {simple_card: 8}},
        {'Player3': {simple_card: 5}}
    ]

    for _ in range(4):
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 0


def test_judgment_set_simple_01(game):
    simple_card1 = 'naghshe' + e_naghshe
    simple_card2 = 'ganj' + e_ganj
    info = [
        {'Player0': {simple_card1: 13}},
        {'Player1': {simple_card2: 8}},
        {'Player2': {simple_card1: 5}},
        {'Player3': {simple_card2: 1}}
    ]

    for _ in range(2):
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 1
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 0


def test_judgment_set_simple_02(game):
    simple_card1 = 'ganj' + e_ganj
    simple_card2 = 'tooti' + e_tooti
    info = [
        {'Player0': {simple_card1: 1}},
        {'Player1': {simple_card1: 7}},
        {'Player2': {simple_card1: 10}},
        {'Player3': {simple_card2: 5}}
    ]

    info.insert(0, info.pop())
    assert judgment_set(info, game) == 3
    for _ in range(3):
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 2


def test_judgment_set_simple_03(game):
    simple_card1 = 'naghshe' + e_naghshe
    simple_card2 = 'ganj' + e_ganj
    simple_card3 = 'tooti' + e_tooti
    info = [
        {'Player0': {simple_card1: 13}},
        {'Player1': {simple_card2: 12}},
        {'Player2': {simple_card3: 11}}
    ]

    for i in range(2):
        print(i)
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 2-i


def test_judgment_set_jolly_00(game):
    jolly_card = 'Jolly Roger' + e_Jolly_Roger
    info = [
        {'Player0': {jolly_card: 13}},
        {'Player1': {jolly_card: 1}},
        {'Player2': {jolly_card: 8}},
        {'Player3': {jolly_card: 5}}
    ]

    for _ in range(4):
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 0


def test_judgment_set_jolly_01(game):
    simple_card = 'naghshe' + e_naghshe
    jolly_card = 'Jolly Roger' + e_Jolly_Roger
    info = [
        {'Player0': {jolly_card: 1}},
        {'Player1': {simple_card: 13}},
        {'Player2': {simple_card: 5}},
        {'Player3': {simple_card: 8}}
    ]

    for _ in range(4):
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 0


def test_judgment_set_jolly_02(game):
    simple_card = 'naghshe' + e_naghshe
    jolly_card = 'Jolly Roger' + e_Jolly_Roger
    info = [
        {'Player0': {jolly_card: 9}},
        {'Player1': {simple_card: 13}},
        {'Player2': {jolly_card: 5}},
        {'Player3': {simple_card: 8}}
    ]

    for _ in range(4):
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 0


def test_judgment_set_jolly_03(game):
    simple_card = 'naghshe' + e_naghshe
    jolly_card = 'Jolly Roger' + e_Jolly_Roger
    info = [
        {'Player0': {simple_card: 13}},
        {'Player1': {jolly_card: 9}},
        {'Player2': {jolly_card: 12}},
        {'Player3': {jolly_card: 5}}
    ]

    for _ in range(4):
        info.insert(0, info.pop())
        assert judgment_set(info, game) == 2
