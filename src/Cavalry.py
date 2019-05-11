from src.AbstractUnit import AbstractUnit


class Cavalry(AbstractUnit):
    def __init__(self, country, country_march):
        super().__init__(country)
        self._country_march = country_march

    def get_attack_message(self):
        return "Cavalry, to the horses!"

    def get_march_message(self):
        return self._country + " Cavalry march! " + self._country_march
