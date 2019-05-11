from src.UnitFactory import UnitFactory
from src.Archer import Archer
from src.Cavalry import Cavalry
from src.Swordsman import Swordsman
from src.CountriesConstants import GREAT_BRITAIN


class EnglishUnitFactory(UnitFactory):
    def create_archers(self):
        return Archer(GREAT_BRITAIN.FLAG)

    def create_cavalry(self):
        return Cavalry(GREAT_BRITAIN.FLAG, GREAT_BRITAIN.MARCH)

    def create_swordsmen(self):
        return Swordsman(GREAT_BRITAIN.FLAG)
