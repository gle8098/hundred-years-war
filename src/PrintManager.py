from src.BattleEventsListener import BattleEventsListener


class PrintManager(BattleEventsListener):
    _inst = None

    @staticmethod
    def inst():
        if PrintManager._inst is None:
            PrintManager._inst = PrintManager()
        return PrintManager._inst

    def info(self, army, text):
        print('[{}] {}'.format(army.get_country().FLAG, text))

    def global_info(self, text):
        print('[GLOBAL] {}'.format(text))

    def on_reflected_attack(self, attack_obj):
        self.info(attack_obj.attacking.get_army(), '{} reflected the attack via protection'.
                  format(str(attack_obj.attacking)))

    def on_unit_damaged(self, attack_obj):
        self.info(attack_obj.attacking.get_army(), 'The attack hurt {} by {}'.
                  format(str(attack_obj.attacking), attack_obj.damage))

    def on_unit_killed(self, attack_obj):
        self.info(attack_obj.attacking.get_army(), '{} died in attack of {}'.format(
            str(attack_obj.attacking), str(attack_obj.attacker)))

    def on_squad_killed(self, attack_obj):
        self.info(attack_obj.attacking.get_army(), 'have lost a good unit {}'.format(str(attack_obj.attacking)))

    def print_armies(self, english_army, french_army):
        print('ENGLISH ARMY')
        print(str(english_army))
        print('FRENCH ARMY')
        print(str(french_army))
