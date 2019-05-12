class BattleEventsListener:
    def on_battle_begins(self):
        pass

    def on_battle_ends(self):
        pass

    def on_reflected_attack(self, attack_obj):
        pass

    def on_unit_damaged(self, attack_obj):
        pass

    def on_unit_killed(self, attack_obj):
        pass

    def on_squad_killed(self, attack_obj):
        pass
