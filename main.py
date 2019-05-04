class Game:
    _inst = None

    @staticmethod
    def inst():
        if Game._inst is None:
            Game._inst = Game()
        return Game._inst

    def init(self):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    Game.inst().init()
    Game.inst().run()
    from tests.Game_class import TestGame
    TestGame.game_inst_method(None)
