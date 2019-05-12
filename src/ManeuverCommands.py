from random import randint


class ManeuverCommand:
    def execute(self, attacking, attacked_army):
        pass


class AbstractManeuverCommand(ManeuverCommand):
    def get_attacking_squad(self, attacking, attacked_army):
        pass

    def execute(self, attacking, attacked_army):
        attacked = self.get_attacking_squad(attacking, attacked_army)
        if attacked is None:
            return
        attack_obj = attacking.attack_initiator(attacked)
        attacked_army.take_strike(attack_obj)


class AttackRandomManeuverCommand(AbstractManeuverCommand):
    def get_attacking_squad(self, attacking, attacked_army):
        return attacked_army.get_random_squad()


class AttackLeastHealthyManeuverCommand(AbstractManeuverCommand):
    def get_attacking_squad(self, attacking, attacked_army):
        return attacked_army.find_least_healthy_squad()


class AttackMostHelathyManeuverCommand(AbstractManeuverCommand):
    def get_attacking_squad(self, attacking, attacked_army):
        return attacked_army.find_most_healthy_squad()


def generate_random_maneuver_command():
    maneuver_id = randint(1, 3)
    if maneuver_id == 1:
        return AttackRandomManeuverCommand()
    elif maneuver_id == 2:
        return AttackLeastHealthyManeuverCommand()
    elif maneuver_id == 3:
        return AttackMostHelathyManeuverCommand()
