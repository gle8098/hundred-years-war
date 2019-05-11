from src.Unit import Unit
from src.Archer import Archer
from src.Army import Army
from src.Squad import Squad
from src.ArmyEconomics import EconomicDevelopmentParameters


class MagicArcherDecorator(Unit):
    _archer = None

    def __init__(self, archer: Archer):
        self._archer = archer

    def attack(self, enemy):
        self._archer.attack(enemy)
        army: Army = self._archer.get_squad().get_army()
        squad_to_treat: Squad = army.find_least_healthy_squad()
        if squad_to_treat is not None:
            for unit in squad_to_treat.get_units():
                unit.update_health(EconomicDevelopmentParameters.ARCHERS_TREAT_HEALTH)

    def get_country(self):
        return self._archer.get_country()

    def get_squad(self):
        return self._archer.get_squad()

    def get_health(self):
        return self._archer.get_health()

    def get_protection(self):
        return self._archer.get_protection()

    def get_attack_message(self):
        return self._archer.get_attack_message()

    def get_march_message(self):
        return self._archer.get_march_message()

    def on_attack(self, attacker):
        return self._archer.on_attack(attacker)

    def update_health(self, delta_health):
        return self._archer.update_health(delta_health)
