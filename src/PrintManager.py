from src.Army import Army
from src.BattleEventsListener import BattleEventsListener
from src.CombatElement import CombatElement


class PrintManager(BattleEventsListener):
    _inst = None

    @staticmethod
    def inst():
        if PrintManager._inst is None:
            PrintManager._inst = PrintManager()
        return PrintManager._inst

    def info(self, army: Army, text: str):
        print('[{}] {}'.format(army.get_country().FLAG, text))

    def on_combat_element_died(self, poor_fellow: CombatElement):
        self.info(poor_fellow.get_army(), 'have lost a good unit {}'.format(str(poor_fellow)))
