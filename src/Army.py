from src.ArmyEconomics import ArmyEconomics
from src.Squad import Squad
from src.ArmyEconomicsProxy import ArmyEconomicsProxy
from src.CountriesConstants import CountryConstants
from src.CombatElement import CombatElement
from src.BattleEventsListener import BattleEventsListener


class Army:
    _country: CountryConstants = None
    _squads = None
    _unitFactory = None
    _coins = None
    _is_battle_state = False
    _economics = None
    _subscribers = []

    def __init__(self):
        self._economics = ArmyEconomicsProxy(self, ArmyEconomics(self))

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

    def _find_most_squad(self, comparator) -> Squad:
        result: Squad = None
        for squad in self._squads:
            if result is None or comparator(squad.get_health(), result.get_health()):
                result = squad
        return result

    def find_least_healthy_squad(self) -> Squad:
        return self._find_most_squad(lambda x, y: x < y)

    def find_most_healthy_squad(self) -> Squad:
        return self._find_most_squad(lambda x, y: x > y)

    def get_random_squad(self) -> Squad:
        from random import randint
        return self._squads[randint(0, len(self._squads) - 1)]

    def get_squads(self):
        return tuple(self._squads)

    def is_in_battle(self):
        return self._is_battle_state

    def add_battle_events_subscriber(self, subscriber):
        if not isinstance(subscriber, BattleEventsListener):
            raise TypeError("Subscriber is not instance of BattleEventsListener")
        self._subscribers.append(subscriber)

    def remove_battle_events_subscriber(self, subscriber):
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
            return True
        return False

    def _send_event(self, event_sender):
        for subscriber in self._subscribers:
            event_sender(subscriber)

    def on_attack(self, attacked: Squad, damage: int, attacking: CombatElement):
        if attacked not in self._squads:
            raise ValueError("Attacked squad in not is this army")
        alive = attacked.take_strike(attacking, damage)
        if not alive:
            self._squads.remove(attacked)
            self._send_event(lambda listener: listener.on_combat_element_died(attacked))

