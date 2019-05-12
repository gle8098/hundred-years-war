from src.AbstractUnit import AbstractUnit


class Swordsman(AbstractUnit):
    def __init__(self, squad):
        super().__init__(squad)

    def get_attack_message(self):
        return "Swordsmen, get ready!"

    def get_march_message(self):
        return self._squad.get_army().get_country().FLAG + " will have the victory!"
