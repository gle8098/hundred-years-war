from src.AbstractUnit import AbstractUnit


class Archer(AbstractUnit):
    def __init__(self, squad):
        super().__init__(squad)

    def get_attack_message(self):
        return "Arrows on bows!"

    def get_march_message(self):
        return "Pchiushhhhh."
