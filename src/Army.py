from src.ArmyEconomics import ArmyEconomics
from src.Squad import Squad


class Army:
    _country = None # type of CountryConstants
    _squads = None
    _unitFactory = None
    _coins = None
    is_war_state = False

    def __init__(self):
        ArmyEconomics(self)

    def get_country(self):
        return self._country

    def get_unit_factory(self):
        return self._unitFactory

    def get_coins_count(self):
        return self._coins

    def spend_coins(self, amount):
        if self._coins >= amount:
            self._coins -= amount
            return True
        return False

    def find_least_healthy_squad(self):
        result: Squad = None
        for squad in self._squads:
            if result is None or result.get_health() > squad.get_health():
                result = squad
        return result

    def is_in_war(self):
        return self.is_war_state
