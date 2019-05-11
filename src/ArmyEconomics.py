from src.Army import Army
from src.Unit import Unit
from src.Archer import Archer
from src.MagicArcherDecorator import MagicArcherDecorator
from src.ArmyEconomicsDevelopment import ArmyEconomicsDevelopment


class EconomicDevelopmentParameters:
    # Увеличивает начальное здоровье всех юнитов из одного отряда
    UPGRADE_HEALTH_PRICE = 50
    HEALTH_INCREASE = 20

    # Увеличивает начальную броню всех юнитов из одного отряда
    UPGRADE_PROTECTION_PRICE = 40
    PROTECTION_INCREASE = 20

    # Добавляет возможность отряду лучников лечить другой отряд из армии с наименьшим здоровьем
    UPGRADE_ARCHERS_PRICE = 100
    ARCHERS_TREAT_HEALTH = 5 # на столько лучники будут вылечивать отряд


class ArmyEconomics(ArmyEconomicsDevelopment):
    _army = None

    def __init__(self, army: Army):
        self._army = army

    def upgrade_health(self, squad):
        if self._army.spend_coins(EconomicDevelopmentParameters.UPGRADE_HEALTH_PRICE):
            squad.update_init_health(EconomicDevelopmentParameters.HEALTH_INCREASE)
            return True
        return False

    def upgrade_protection(self, squad):
        if self._army.spend_coins(EconomicDevelopmentParameters.UPGRADE_PROTECTION_PRICE):
            squad.update_init_protection(EconomicDevelopmentParameters.PROTECTION_INCREASE)
            return True
        return False

    def upgrade_archers(self, archer: Unit):
        if not isinstance(archer, Archer):
            raise TypeError("Only Archers can be upgraded in this way")

        if self._army.spend_coins(EconomicDevelopmentParameters.UPGRADE_ARCHERS_PRICE):
            magic_archer = MagicArcherDecorator(archer)
            archer.get_squad().replace_unit(archer, magic_archer)
        return False
