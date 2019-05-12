from src.Army import Army
from src import GameplayParameters
from src.Battle import Battle
from src.Squad import Squad
from src.ArmyAssembler import ArmyAssembler
import src
import time
import pytest


def load_test(squads_count, units_count, capsys):
    armies = [Army(src.CountriesConstants.GREAT_BRITAIN, src.EnglishUnitFactory.EnglishUnitFactory()),
              Army(src.CountriesConstants.FRANCE, src.FrenchUnitFactory.FrenchUnitFactory())]
    for army in armies:
        for _ in range(squads_count):
            squad = Squad(army)
            for _ in range(units_count):
                unit = ArmyAssembler.create_random_unit(army.get_unit_factory(), squad)
                squad.add_unit(unit)
            army.add_squad(squad)
    battle = Battle(armies[0], armies[1])

    start = time.time()
    battle.begin_battle()
    duration = time.time() - start
    with capsys.disabled():
        print('\nBattle with {} squads each with {} units took {}s'.format(squads_count, units_count, duration))


@pytest.mark.loadtest
def test_load_test_25_10(capsys):
    load_test(25, 10, capsys)


@pytest.mark.loadtest
def test_load_100_10(capsys):
    load_test(100, 10, capsys)


@pytest.mark.loadtest
def test_load_10_1000(capsys):
    load_test(10, 1000, capsys)
