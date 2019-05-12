from src.Army import Army
from src import GameplayParameters
import src


class FictionSquad:
    updated = False

    def update_init_health(self, val):
        self.updated = True

    def update_init_protection(self, val):
        self.updated = True

    def replace_unit(self, val1, val2):
        self.updated = True


class FictionArcher(src.Archer.Archer):
    squad = None

    def __init__(self):
        self.squad = FictionSquad()

    def get_squad(self):
        return self.squad


def test_economics_proxy():
    army = Army(src.CountriesConstants.GREAT_BRITAIN, None)
    army.income(2 * (GameplayParameters.UPGRADE_HEALTH_PRICE + GameplayParameters.UPGRADE_ARCHERS_PRICE +
                     GameplayParameters.UPGRADE_PROTECTION_PRICE))
    economy = army.economics_development()
    sq = FictionSquad()

    # Health
    assert economy.upgrade_health(sq)
    assert sq.updated
    sq.updated = False
    army.set_martial_law()
    assert not economy.upgrade_health(sq)
    assert not sq.updated
    army.remove_martial_law()

    # Protection
    assert economy.upgrade_protection(sq)
    assert sq.updated
    sq.updated = False
    army.set_martial_law()
    assert not economy.upgrade_protection(sq)
    assert not sq.updated
    army.remove_martial_law()

    # Archer
    arch = FictionArcher()
    assert economy.upgrade_archers(arch)
    assert arch.get_squad().updated
    arch.get_squad().updated = False
    army.set_martial_law()
    assert not economy.upgrade_archers(arch)
    assert not arch.get_squad().updated
    army.remove_martial_law()
