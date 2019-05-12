from src.Army import Army


class CombatElement:
    # Запускает процесс удара: юнит/отряд что-то делает и возвращает суммарное количество урона, которое он наносит
    def attack_initiator(self, enemy: 'CombatElement'):
        pass

    # Принимает удар, нанесенный attacker. Метод должен рассчитать свое новое здоровье и вернуть True, если остался жив.
    def take_strike(self, attacker: 'CombatElement', damage: int):
        pass

    def get_health(self):
        pass

    def get_army(self) -> Army:
        pass

    # Обновляет параметры перед новой битвой. Такие как, например, здоровье.
    def reset_battle_parameters(self):
        pass
