from src.CombatElement import CombatElement
from src.Attack import Attack
from src import GameplayParameters


class Squad(CombatElement):
    _army = None
    _units = None
    _init_health = GameplayParameters.INITIAL_SQUAD_HEALTH
    _init_protection = GameplayParameters.INITIAL_SQUAD_PROTECTION

    def __init__(self, army):
        self._army = army
        self._units = []

    # Getters & Setters

    def get_army(self):
        return self._army

    def get_country(self):
        return self._army.get_country()

    def get_protection(self):
        res = 0
        for unit in self._units:
            res += unit.get_protection()
        return res

    def get_init_health(self):
        return self._init_health

    def get_init_protection(self):
        return self._init_protection

    def update_init_health(self, health_delta):
        self._init_health += health_delta
        self.reset_battle_parameters()

    def update_init_protection(self, protect_delta):
        self._init_protection += protect_delta
        self.reset_battle_parameters()

    def add_unit(self, unit):
        self._units.append(unit)

    def replace_unit(self, old_unit, new_unit):
        self._units.remove(old_unit)
        self._units.append(new_unit)

    def get_units(self):
        return tuple(self._units)

    def get_health(self):
        common_health = 0
        for unit in self._units:
            common_health += unit.get_health()
        return common_health

    # Battle Related

    def reset_battle_parameters(self):
        for unit in self._units:
            unit.reset_battle_parameters()

    def attack_initiator(self, enemy):
        result = Attack(self, enemy, 0)
        for unit in self._units:
            result.damage += unit.attack_initiator(enemy).damage
        return result

    def take_strike(self, attack):
        if not self.is_alive():
            return False

        alive = False
        for unit in self._units:
            if not unit.is_alive():
                continue
            attack.attacking = unit
            alive = unit.take_strike(attack)
            if not alive:
                self._army.on_attacked_result(attack, self._army.ATTACK_EVENT_TYPES['unit_killed'])
            if attack.damage <= 0:
                alive = True
                break

        if not alive:
            self._army.on_attacked_result(attack, self._army.ATTACK_EVENT_TYPES['squad_killed'])

        return alive

    # To String

    def __str__(self):
        res = 'Squad ['
        for unit in self._units:
            res += str(unit) + ', '
        return res[:-2] + ']'
