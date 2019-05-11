from src.Unit import Unit


class AbstractUnit(Unit):
    _country = None
    _squad = None
    _health = None
    _protection = None

    def __init__(self, squad, country):
        self._squad = squad
        self._country = country
        self._health = squad.get_init_health()
        self._protection = squad.get_init_protection()

    def get_country(self):
        return self._country

    def get_squad(self):
        return self._squad

    def get_health(self):
        return self._health

    def get_protection(self):
        return self._protection

    def get_attack_message(self):
        pass

    def get_march_message(self):
        pass
