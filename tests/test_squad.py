from src.Squad import Squad
import src


def test_squad_getters():
    country = src.CountriesConstants.FRANCE
    army = src.Army.Army(country, None)
    sq = Squad(army)
    assert (sq.get_country() == country)
    assert (sq.get_army() == army)
    assert (sq.get_init_health() == src.GameplayParameters.INITIAL_SQUAD_HEALTH)
    assert (sq.get_init_protection() == src.GameplayParameters.INITIAL_SQUAD_PROTECTION)
    assert (sq.get_health() == 0)
    assert (sq.get_protection() == 0)
    assert (len(sq.get_units()) == 0)

    sq.update_init_health(10)
    sq.update_init_protection(50)

    assert (sq.get_init_health() == src.GameplayParameters.INITIAL_SQUAD_HEALTH + 10)
    assert (sq.get_init_protection() == src.GameplayParameters.INITIAL_SQUAD_PROTECTION + 50)

    sq.add_unit(None)
    assert (sq.get_units() == (None,))


def test_squad_battle_related():
    country = src.CountriesConstants.FRANCE
    army = src.Army.Army(country, None)
    sq = Squad(army)
    units = (src.Archer.Archer(sq), src.Archer.Archer(sq), src.Swordsman.Swordsman(sq))
    for unit in units:
        sq.add_unit(unit)
    units[0].update_health(-1000)
    sq.reset_battle_parameters()

    assert (sq.get_health() == 3 * src.GameplayParameters.INITIAL_SQUAD_HEALTH)

    attack = sq.attack_initiator(country)
    assert (attack.attacking == country)
    assert (attack.damage == 2 * src.Archer.Archer.ATTACKING_DAMAGE + src.Swordsman.Swordsman.ATTACKING_DAMAGE)
    assert (attack.attacker == sq)

