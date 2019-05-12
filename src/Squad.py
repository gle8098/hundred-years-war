from src.CombatElement import CombatElement
from src.Army import Army
from src.BattleEventsListener import BattleEventsListener


class Squad(CombatElement, BattleEventsListener):
    INITIAL_HEALTH = 100
    INITIAL_PROTECTION = 5

    _army: Army = None
    _units = []
    _init_health = INITIAL_HEALTH
    _init_protection = INITIAL_PROTECTION

    def get_army(self):
        return self._army

    def get_init_health(self):
        return self._init_health

    def get_init_protection(self):
        return self._init_protection

    def update_init_health(self, health_delta):
        self._init_health += health_delta

    def update_init_protection(self, protect_delta):
        self._init_protection += protect_delta

    def replace_unit(self, old_unit, new_unit):
        self._units.pop(old_unit)
        self._units.append(new_unit)

    def get_units(self):
        return tuple(self._units)

    def get_health(self):
        commonHealth = 0
        for unit in self._units:
            commonHealth += unit.get_health()
        return commonHealth

    def on_battle_begins(self):
        self.reset_battle_parameters()

    def reset_battle_parameters(self):
        for unit in self._units:
            unit.reset_battle_parameters()

    def __str__(self):
        res = 'Squad ['
        for unit in self._units:
            res += str(unit) + ', '
        return res[:-2] + ']'
