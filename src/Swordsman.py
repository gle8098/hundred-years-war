from src.AbstractUnit import AbstractUnit


class Swordsman(AbstractUnit):
    def __init__(self, country):
        super().__init__(country)

    def get_attack_message(self):
        return "Swordsmen, get ready!"

    def get_country(self):
        return self._country

    def get_march_message(self):
        return self._country + " will have the victory!"
