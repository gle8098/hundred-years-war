from src.ArmyEconomicsDevelopment import ArmyEconomicsDevelopment
from src.Army import Army


# Класс блокирует любые обращения к развитию экономики в военное время
class ArmyEconomicsProxy(ArmyEconomicsDevelopment):
    _army: Army = None
    _economics: ArmyEconomicsDevelopment = None

    def __init__(self, army, economics):
        self._army = army
        self._economics = economics

    def upgrade_health(self, squad):
        if self._army.is_in_battle():
            return False
        return self._economics.upgrade_health(squad)

    def upgrade_protection(self, squad):
        if self._army.is_in_battle():
            return False
        return self._economics.upgrade_protection(squad)

    def upgrade_archers(self, archer):
        if self._army.is_in_battle():
            return False
        return self._economics.upgrade_archers(archer)
