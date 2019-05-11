from src.AbstractUnit import AbstractUnit


class Archer(AbstractUnit):
    def __init__(self, country):
        super().__init__(country) # todo

    def get_attack_message(self):
        return "Arrows on bows!"

    def get_country(self):
        return self._country

    def get_march_message(self):
        return "Pchiushhhhh."
