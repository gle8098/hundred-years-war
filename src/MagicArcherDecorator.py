from src.Unit import Unit
from src import GameplayParameters
from src.PrintManager import PrintManager


class MagicArcherDecorator(Unit):
    _archer = None

    def __init__(self, archer):
        self._archer = archer

    def attack_initiator(self, enemy):
        result = self._archer.attack_initiator(enemy)
        army = self._archer.get_squad().get_army()
        squad_to_treat = army.find_least_healthy_squad()
        if squad_to_treat is not None:
            for unit in squad_to_treat.get_units():
                unit.update_health(GameplayParameters.ARCHERS_TREAT_HEALTH)
            PrintManager.inst().info(self._archer.get_army(), 'Magic! {} treats squad!'.format(str(self)))
        result.attacker = self
        return result

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

    def update_health(self, delta_health):
        return self._archer.update_health(delta_health)

    def take_strike(self, attack):
        attack.attacking = self._archer
        result = self._archer.take_strike(attack)
        attack.attacking = self
        return result

    def get_army(self):
        return self._archer.get_army()

    def reset_battle_parameters(self):
        return self._archer.reset_battle_parameters()

    def get_country(self):
        return self._archer.get_country()

    def __str__(self):
        return 'Magic' + str(self._archer)
