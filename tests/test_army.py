from src.Army import Army
from src import GameplayParameters
import src


class FictionSquad(src.CombatElement.CombatElement):
    health = 10
    reset = False

    def get_health(self):
        return self.health

    def reset_battle_parameters(self):
        self.reset = True


class EventListener(src.BattleEventsListener.BattleEventsListener):
    battle_begins = False
    battle_ends = False
    squad_died = False

    def on_battle_begins(self):
        self.battle_begins = True

    def on_battle_ends(self):
        self.battle_ends = True

    def on_squad_died(self, attack_obj):
        assert isinstance(attack_obj, src.Attack.Attack)
        self.squad_died = True


def test_army():
    army = Army(src.CountriesConstants.FRANCE, None)

    assert (army.get_country().ID == 2)
    assert (army.is_in_battle() is False)
    assert (isinstance(army.economics_development(), src.ArmyEconomicsDevelopment.ArmyEconomicsDevelopment))

    assert (army.get_coins_count() == GameplayParameters.INITIAL_MONEY_COUNT)
    army.spend_coins(50)
    army.income(30)
    assert (army.get_coins_count() == GameplayParameters.INITIAL_MONEY_COUNT - 20)

    sq1 = FictionSquad()
    sq2 = FictionSquad()
    sq2.health = 20
    army.add_squad(sq1)
    army.add_squad(sq2)
    assert (army.get_health() == 30)
    assert (army.find_least_healthy_squad().get_health() == 10)
    assert (army.find_most_healthy_squad().get_health() == 20)
    army.reset_battle_parameters()
    assert sq1.reset
    assert sq2.reset

    ev1 = EventListener()
    ev2 = EventListener()
    army.add_battle_events_subscriber(ev1)
    army.add_battle_events_subscriber(ev2)
    army.set_martial_law()
    assert ev1.battle_begins
    assert ev2.battle_begins
    assert army.remove_battle_events_subscriber(ev2)
    army.remove_martial_law()
    assert ev1.battle_ends
    assert not ev2.battle_ends

    army.set_martial_law()
    assert army.is_in_battle() is True
    army.remove_martial_law()
    assert army.is_in_battle() is False
