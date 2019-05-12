import pytest

from src.main import Game
from tests.test_load_tesing import load_test


@pytest.mark.stresstest
def test_stress_test_50_100(capsys):
    load_test(50, 100, capsys)


@pytest.mark.stresstest
def test_monkey_test(capsys, monkeypatch):
    counter = 0

    def test_input():
        from random import randint
        nonlocal counter

        counter += 1
        if counter > 100:
            return '4'  # to run exit from main menu
        return str(randint(1, 3))

    monkeypatch.setattr('builtins.input', test_input)
    game = Game()
    game.init()
    with capsys.disabled():
        game.run()
