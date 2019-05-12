from src.ArmyEconomics import ArmyEconomics
from src.Squad import Squad
from src.ArmyEconomicsProxy import ArmyEconomicsProxy
from src.CountriesConstants import CountryConstants
from src.CombatElement import CombatElement
from src.BattleEventsListener import BattleEventsListener
from src import GameplayParameters


class Army(CombatElement):
    _country: CountryConstants = None
    _squads = None
    _unit_factory = None
    _coins = GameplayParameters.INITIAL_MONEY_COUNT
    _is_battle_state = False
    _economics = None
    _subscribers = None

    def __init__(self, country, unit_factory):
        self._squads = []
        self._country = country
        self._unit_factory = unit_factory
        self._economics = ArmyEconomicsProxy(self, ArmyEconomics(self))
        self._subscribers = []

    # Base Getters

    def get_country(self):
        return self._country

    def get_unit_factory(self):
        return self._unit_factory

    def get_coins_count(self):
        return self._coins

    def economics_development(self):
        return self._economics

    def is_in_battle(self):
        return self._is_battle_state

    def get_health(self):
        result = 0
        for squad in self._squads:
            result += squad.get_health()
        return result

    # Coins Work

    def spend_coins(self, amount):
        if self._coins >= amount:
            self._coins -= amount
            return True
        return False

    def income(self, coins):
        self._coins += coins

    # Squad Related

    def add_squad(self, squad):
        self._squads.append(squad)

    def _get_alive_squards(self):
        result = []
        for squad in self._squads:
            if squad.is_alive():
                result.append(squad)
        return result

    def _find_most_squad(self, comparator) -> Squad:
        result = None
        for squad in self._get_alive_squards():
            if result is None or comparator(squad.get_health(), result.get_health()):
                result = squad
        return result

    def find_least_healthy_squad(self) -> Squad:
        return self._find_most_squad(lambda x, y: x < y)

    def find_most_healthy_squad(self) -> Squad:
        return self._find_most_squad(lambda x, y: x > y)

    def get_random_squad(self):
        from random import randint
        arr = self._get_alive_squards()
        if len(arr) is 0:
            return None
        return arr[randint(0, len(arr) - 1)]

    def get_squads(self):
        return tuple(self._squads)

    # Event Bus Related

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

    ATTACK_EVENT_TYPES = {'reflect': 1, 'damage': 2, 'unit_killed': 3, 'squad_killed': 4}

    def on_attacked_result(self, attack_obj, event_type):
        def handler(listener):
            if event_type == Army.ATTACK_EVENT_TYPES['reflect']:
                listener.on_reflected_attack(attack_obj)
            elif event_type == Army.ATTACK_EVENT_TYPES['damage']:
                listener.on_unit_damaged(attack_obj)
            elif event_type == Army.ATTACK_EVENT_TYPES['unit_killed']:
                listener.on_unit_killed(attack_obj)
            elif event_type == Army.ATTACK_EVENT_TYPES['squad_killed']:
                listener.on_squad_killed(attack_obj)
            else:
                raise ValueError("Unknown event type")
        self._send_event(handler)

    # Battle Related

    def set_martial_law(self):
        self._is_battle_state = True
        self._send_event(lambda listener: listener.on_battle_begins())

    def remove_martial_law(self):
        self._is_battle_state = False
        self._send_event(lambda listener: listener.on_battle_ends())
        self.reset_battle_parameters()

    def take_strike(self, attack):
        if attack.attacking not in self._squads:
            raise ValueError("Attacked squad in not is this army")
        attack.attacking.take_strike(attack)
        return self.is_alive()

    def reset_battle_parameters(self):
        for squad in self._squads:
            squad.reset_battle_parameters()

    # To String

    def __str__(self):
        res = 'Army[coins={}]:\n'.format(self._coins)
        for squad in self._squads:
            res += '  ' + str(squad) + "\n"
        return res
