from src.main import Game


class TestGame:
    def test_game_inst_method(self):
        assert(Game.inst() is Game.inst())
