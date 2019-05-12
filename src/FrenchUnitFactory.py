from src.UnitFactory import UnitFactory
from src.Archer import Archer
from src.Cavalry import Cavalry
from src.Swordsman import Swordsman
from src.CountriesConstants import FRANCE


class FrenchUnitFactory(UnitFactory):
    def create_archers(self, squad):
        return Archer(squad)

    def create_cavalry(self, squad):
        return Cavalry(squad)

    def create_swordsmen(self, squad):
        return Swordsman(squad)
