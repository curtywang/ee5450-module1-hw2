from blackjack_db import AsyncBlackjackGameDB
import pytest
import asyncio


@pytest.fixture
def base_db():
    return AsyncBlackjackGameDB()


@pytest.mark.asyncio
async def test_add_game(base_db):
    game_uuid, game_term_password = await base_db.add_game(1, 2)
    assert len(game_uuid) == 36
    assert len(game_term_password) == 36
    assert base_db._termination_passwords[game_uuid] == game_term_password
    assert base_db._current_games[game_uuid].num_players == 1


@pytest.fixture
async def single_game_db(base_db):
    game_uuid, game_term_password = await base_db.add_game(1)
    return base_db, game_uuid, game_term_password


@pytest.mark.asyncio
async def test_list_games(single_game_db):
    list_of_games = await single_game_db[0].list_games()
    assert len(list_of_games) == 1


@pytest.mark.asyncio
async def test_get_game(single_game_db):
    assert await single_game_db[0].get_game(single_game_db[1]) is not None
    assert await single_game_db[0].get_game(single_game_db[1]) == single_game_db[0]._current_games[single_game_db[1]]


@pytest.mark.asyncio
async def test_del_game(single_game_db):
    assert await single_game_db[0].del_game(single_game_db[1], 'bad_password') is False
    assert await single_game_db[0].del_game(single_game_db[1], single_game_db[2]) is True


if __name__ == '__main__':
    pytest.main()
