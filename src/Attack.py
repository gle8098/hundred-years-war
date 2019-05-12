class Attack:
    attacker = None
    attacking = None
    damage = None

    def __init__(self, attacker, attacking, damage):
        self.attacker = attacker
        self.attacking = attacking
        self.damage = damage
