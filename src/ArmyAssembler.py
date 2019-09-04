from src.Squad import Squad
from src.PrintManager import PrintManager
from random import randint


# Создает армии: по пользовательским данным или рандомно
class ArmyAssembler:
    @staticmethod
    def assemble_armies(english_army, french_army):
        print('Welcome to the army assembler manager! This tool will help you create armies.')
        # print('Do you want armies to be randomly created for you? [y/n]')
        # ans = input()
        if True:  # ans == 'y':
            ArmyAssembler.generate_randomly(english_army)
            ArmyAssembler.generate_randomly(french_army)
            print('Armies were created randomly.')
            PrintManager.inst().print_armies(english_army, french_army)
            return
        # else: todo

    @staticmethod
    def generate_randomly(army):
        squad_count = randint(1, 5)
        for i in range(squad_count):
            squad = Squad(army)
            units_count = randint(1, 4)
            for j in range(units_count):
                squad.add_unit(ArmyAssembler.create_random_unit(army.get_unit_factory(), squad))
            army.add_squad(squad)

    @staticmethod
    def create_random_unit(unit_factory, squad):
        unit_type = randint(1, 3)
        if unit_type == 1:
            return unit_factory.create_cavalry(squad)
        elif unit_type == 2:
            return unit_factory.create_swordsmen(squad)
        else:
            return unit_factory.create_archers(squad)
