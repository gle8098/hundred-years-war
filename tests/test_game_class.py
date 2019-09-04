from src.main import Game


class TestGame:
    def test_init_method(self):
        game = Game()
        game.init()
        assert(game._english_army is not None and game._french_army is not None)
        assert(game._english_army is not game._french_army)
