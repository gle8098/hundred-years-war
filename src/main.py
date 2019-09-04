from src import CountriesConstants
from src.Army import Army
from src.EnglishUnitFactory import EnglishUnitFactory
from src.FrenchUnitFactory import FrenchUnitFactory
from src.PrintManager import PrintManager
from src.ArmyAssembler import ArmyAssembler
from src.Archer import Archer
from src import GameplayParameters as economics_params
from src.Battle import Battle


class Game:
    _english_army = None
    _french_army = None

    def init(self):
        self._english_army = Army(CountriesConstants.GREAT_BRITAIN, EnglishUnitFactory())
        self._french_army = Army(CountriesConstants.FRANCE, FrenchUnitFactory())
        self._english_army.add_battle_events_subscriber(PrintManager.inst())
        self._french_army.add_battle_events_subscriber(PrintManager.inst())
        PrintManager.inst().global_info('Armies created')

    def run(self):
        ArmyAssembler.assemble_armies(self._english_army, self._french_army)

        while True:
            print('You choose:')
            print('1 - battle')
            print('2 - economics upgrade')
            print('3 - armies status')
            print('4 - exit')
            res = input()
            if res == '3':
                PrintManager.inst().print_armies(self._english_army, self._french_army)
            elif res == '2':
                self._action_economics_upgrade()
            elif res == '1':
                battle = Battle(self._english_army, self._french_army)
                battle.begin_battle()
            elif res == '4':
                break
            else:
                print('No such action')

    def _action_economics_upgrade(self):
        print('Choose army:')
        print('1 - English')
        print('2 - French')
        army_id = input()
        if army_id not in ('1', '2'):
            print('There is no such army')
            return
        army = self._english_army
        if army_id == '2':
            army = self._french_army

        print('Choose upgrade scheme:')
        print('1 - upgrade initial health of a squad. {} coins.'.format(economics_params.UPGRADE_HEALTH_PRICE))
        print('2 - upgrade initial protection of a squad. {} coins.'.format(economics_params.UPGRADE_PROTECTION_PRICE))
        print('3 - make an archer a magic archer. {} coins.'.format(economics_params.UPGRADE_ARCHERS_PRICE))
        print('Your army has now {} coins.'.format(army.get_coins_count()))
        scheme_id = input()
        if scheme_id not in ('1', '2', '3'):
            print('Maybe such scheme will be added in future, but not now')
            return

        squads = []
        archers_in_squads = []
        squads_text = ''
        for squad in army.get_squads():
            if scheme_id == '3':
                has_archers = False
                for unit in squad.get_units():
                    if isinstance(unit, Archer):
                        archers_in_squads.append(unit)
                        has_archers = True
                        break
                if not has_archers:
                    continue
            squads.append(squad)
            squads_text += '{} - {}\n'.format(len(squads), str(squad))
        if scheme_id == '3' and len(squads) == 0:
            print('Sorry, there is no archers in selected army')
            return
        print('Choose squad:')
        print(squads_text, end='')
        squad_id = input()
        if not str.isdecimal(squad_id):
            squad_id = 0
        else:
            squad_id = int(squad_id)
        if squad_id <= 0 or squad_id > len(squads):
            print('Oh no, bad squad id')
            return
        squad = squads[squad_id - 1]

        result = None
        if scheme_id == '1':
            result = army.economics_development().upgrade_health(squad)
        elif scheme_id == '2':
            result = army.economics_development().upgrade_protection(squad)
        elif scheme_id == '3':
            result = army.economics_development().upgrade_archers(archers_in_squads[squad_id - 1])

        if not result:
            print('Upgrade failure. Check your army money!')
        else:
            print('Army upgraded!')
            print(str(army))


if __name__ == '__main__':
    game = Game()
    game.init()
    game.run()
