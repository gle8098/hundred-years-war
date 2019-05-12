from src.Unit import Unit
from src.Squad import Squad


class AbstractUnit(Unit):
    _squad: Squad = None
    _health = None
    _protection = None

    def __init__(self, squad):
        self._squad = squad
        self._health = squad.get_init_health()
        self._protection = squad.get_init_protection()

    def get_squad(self):
        return self._squad

    def get_army(self):
        return self._squad.get_army()

    def get_health(self):
        return self._health

    def get_protection(self):
        return self._protection

    def get_attack_message(self):
        pass

    def get_march_message(self):
        pass

    def __str__(self):
        return type(self).__name__ + '[{}/{}]'.format(self._health, self._squad.get_init_health())
