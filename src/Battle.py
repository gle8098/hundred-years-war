from src.ManeuverCommands import *
from src.PrintManager import PrintManager
from src import GameplayParameters as gameplay_params


class Battle:
    _english_army = None
    _french_army = None

    def __init__(self, english_army, french_army):
        self._english_army = english_army
        self._french_army = french_army

    def begin_battle(self):
        print('Battle begins!')
        armies = (self._english_army, self._french_army)
        for army in armies:
            army.set_martial_law()

        while armies[0].is_alive() and armies[1].is_alive():
            # Maneuver begins
            # for each army for each squad
            print('Maneuver begins')
            for army_id in range(2):
                army = armies[army_id]
                for squad in army.get_squads():
                    generate_random_maneuver_command().execute(squad, armies[1 - army_id])
            print('Maneuver ends')

        print('BATTLE RESULTS')

        eng_alive = armies[0].is_alive()
        fr_alive = armies[1].is_alive()
        if not eng_alive and not fr_alive:
            print('A TIE!')
        elif not eng_alive:
            print('FRANCE WON!')
            print('France wins {} coins, G.B. -- {} coins'.format(gameplay_params.INCOME_ON_WIN, gameplay_params.INCOME_ON_LOSE))
            armies[0].income(gameplay_params.INCOME_ON_WIN)
            armies[1].income(gameplay_params.INCOME_ON_LOSE)
        else:
            print('GREAT BRITAIN WON!')
            print('G.B. wins {} coins, France -- {} coins'.format(gameplay_params.INCOME_ON_WIN, gameplay_params.INCOME_ON_LOSE))
            armies[1].income(gameplay_params.INCOME_ON_WIN)
            armies[0].income(gameplay_params.INCOME_ON_LOSE)

        PrintManager.inst().print_armies(armies[0], armies[1])

        for army in armies:
            army.remove_martial_law()
