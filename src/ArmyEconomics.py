from src import GameplayParameters
from src.Archer import Archer
from src.MagicArcherDecorator import MagicArcherDecorator
from src.ArmyEconomicsDevelopment import ArmyEconomicsDevelopment


class ArmyEconomics(ArmyEconomicsDevelopment):
    _army = None

    def __init__(self, army):
        self._army = army

    def upgrade_health(self, squad):
        if self._army.spend_coins(GameplayParameters.UPGRADE_HEALTH_PRICE):
            squad.update_init_health(GameplayParameters.HEALTH_INCREASE)
            return True
        return False

    def upgrade_protection(self, squad):
        if self._army.spend_coins(GameplayParameters.UPGRADE_PROTECTION_PRICE):
            squad.update_init_protection(GameplayParameters.PROTECTION_INCREASE)
            return True
        return False

    def upgrade_archers(self, archer):
        if not isinstance(archer, Archer):
            raise TypeError("Only Archers can be upgraded in this way")

        if self._army.spend_coins(GameplayParameters.UPGRADE_ARCHERS_PRICE):
            magic_archer = MagicArcherDecorator(archer)
            archer.get_squad().replace_unit(archer, magic_archer)
            return True
        return False
