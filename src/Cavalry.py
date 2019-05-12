from src.AbstractUnit import AbstractUnit


class Cavalry(AbstractUnit):
    ATTACKING_DAMAGE = 30

    def __init__(self, squad):
        super().__init__(squad)

    def get_attack_message(self):
        return "Cavalry, to the horses!"

    def get_march_message(self):
        country = self._squad.get_army().get_country()
        return country.FLAG + " Cavalry march! " + country.MARCH

    def get_attacking_damage(self):
        return Cavalry.ATTACKING_DAMAGE
