from src.AbstractUnit import AbstractUnit
from src.Attack import Attack
from src.Archer import Archer
from src.Swordsman import Swordsman
from src.Cavalry import Cavalry
from src.MagicArcherDecorator import MagicArcherDecorator
from src import GameplayParameters
import src


def unit_test(unit, sq, army):
    assert (unit.get_squad() == sq)
    assert (unit.get_army() == army)
    assert (unit.get_health() == src.GameplayParameters.INITIAL_SQUAD_HEALTH)
    assert (unit.get_protection() == src.GameplayParameters.INITIAL_SQUAD_PROTECTION)

    attack = unit.attack_initiator(None)
    assert (attack.attacker == unit)
    assert (attack.attacking is None)
    if isinstance(unit, MagicArcherDecorator):
        assert (attack.damage == Archer.ATTACKING_DAMAGE)
    else:
        assert (attack.damage is None)

    unit.update_health(-10)
    assert (unit.get_health() == src.GameplayParameters.INITIAL_SQUAD_HEALTH - 10)
    unit.reset_battle_parameters()
    assert (unit.get_health() == src.GameplayParameters.INITIAL_SQUAD_HEALTH)

    init_health = src.GameplayParameters.INITIAL_SQUAD_HEALTH + src.GameplayParameters.INITIAL_SQUAD_PROTECTION
    assert (not unit.take_strike(Attack(None, unit, init_health + 10)))
    assert (unit.get_health() == 0)

    unit.reset_battle_parameters()
    assert (unit.take_strike(Attack(None, unit, init_health - 10)))
    assert (unit.get_health() == 10)


def test_abstract_unit():
    army = src.Army.Army(src.CountriesConstants.FRANCE, None)
    sq = src.Squad.Squad(army)
    unit = AbstractUnit(sq)

    unit_test(unit, sq, army)

    assert (unit.get_attack_message() is None)
    assert (unit.get_attacking_damage() is None)
    assert (unit.get_march_message() is None)


def check_string(string):
    assert (type(string).__name__ == 'str')
    assert (len(string) > 0)


def test_magic_archer():
    army = src.Army.Army(src.CountriesConstants.FRANCE, None)
    sq = src.Squad.Squad(army)
    unit = MagicArcherDecorator(Archer(sq))

    unit_test(unit, sq, army)
    check_string(unit.get_attack_message())
    check_string(unit.get_march_message())


def test_unit_implementations():
    army = src.Army.Army(src.CountriesConstants.FRANCE, None)
    sq = src.Squad.Squad(army)
    impls = (Archer(sq), Swordsman(sq), Cavalry(sq))

    for impl in impls:
        check_string(impl.get_march_message())
        check_string(impl.get_attack_message())
        number = impl.get_attacking_damage()
        assert (type(number).__name__ == 'int')
        assert (number > 0)
