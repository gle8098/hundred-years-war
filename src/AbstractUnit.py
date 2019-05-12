from src.Unit import Unit
from src.Squad import Squad
from src.PrintManager import PrintManager
from src.Attack import Attack


class AbstractUnit(Unit):
    _squad: Squad = None
    _health = None

    def __init__(self, squad):
        self._squad = squad
        self._health = squad.get_init_health()

    def get_squad(self):
        return self._squad

    def get_army(self):
        return self._squad.get_army()

    def get_health(self):
        return self._health

    def get_protection(self):
        return self._squad.get_init_protection()

    def get_attack_message(self):
        pass

    def get_march_message(self):
        pass

    def get_attacking_damage(self):
        pass

    def update_health(self, delta_health):
        self._health += delta_health

    def attack_initiator(self, enemy):
        PrintManager.inst().info(self.get_army(), self.get_attack_message())
        return Attack(self, enemy, self.get_attacking_damage())

    def take_strike(self, attack):
        if attack.attacking is not self:
            raise ValueError("Cannot take strike of attack which is not addressed to me")
        attack.damage -= self.get_protection()
        if attack.damage <= 0:
            self.get_army().on_attacked_result(attack, self.get_army().ATTACK_EVENT_TYPES['reflect'])
            return True
        self._health -= attack.damage
        if self._health > 0:
            self.get_army().on_attacked_result(attack, self.get_army().ATTACK_EVENT_TYPES['damage'])
            attack.damage = 0
            return True
        attack.damage = -self._health
        self._health = 0
        return False

    def reset_battle_parameters(self):
        self._health = self._squad.get_init_health()

    def __str__(self):
        return type(self).__name__ + '[H{}/{}; P{}]'.format(self._health, self._squad.get_init_health(),
                                                            self.get_protection())
