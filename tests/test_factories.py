from src.UnitFactory import UnitFactory
from src.EnglishUnitFactory import EnglishUnitFactory
from src.FrenchUnitFactory import FrenchUnitFactory
from src.Squad import Squad
import src


def test_factories():
    squad = Squad(None)
    for factory in (EnglishUnitFactory(), FrenchUnitFactory()):
        assert(isinstance(factory.create_archers(squad), src.Archer.Archer))
        assert(factory.create_archers(squad) is not factory.create_archers(squad))
        assert(isinstance(factory.create_cavalry(squad), src.Cavalry.Cavalry))
        assert(factory.create_cavalry(squad) is not factory.create_cavalry(squad))
        assert(isinstance(factory.create_swordsmen(squad), src.Swordsman.Swordsman))
        assert(factory.create_swordsmen(squad) is not factory.create_swordsmen(squad))
