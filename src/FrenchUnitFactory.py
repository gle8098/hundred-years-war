from src.UnitFactory import UnitFactory
from src.Archer import Archer
from src.Cavalry import Cavalry
from src.Swordsman import Swordsman
from src.CountriesConstants import FRANCE


class FrenchUnitFactory(UnitFactory):
    def create_archers(self):
        return Archer(FRANCE.FLAG)

    def create_cavalry(self):
        return Cavalry(FRANCE.FLAG, FRANCE.MARCH)

    def create_swordsmen(self):
        return Swordsman(FRANCE.FLAG)
