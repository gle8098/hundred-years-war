from src.CombatElement import CombatElement
from src.Army import Army


class ManeuverCommand:
    def execute(self, attacking: CombatElement, attacked_army: Army):
        pass


class AttackRandomManeuverCommand(ManeuverCommand):
    def execute(self, attacking: CombatElement, attacked_army: Army):
        attacked = attacked_army.get_random_squad()
        damage = attacking.attack_initiator(attacked)
        attacked_army.on_attack(attacked, damage, attacking)
