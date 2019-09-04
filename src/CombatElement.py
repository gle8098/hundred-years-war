class CombatElement:
    # Запускает процесс удара: юнит/отряд что-то делает и возвращает объект Attack
    # enemy -- Squad
    def attack_initiator(self, enemy):
        pass

    # Принимает удар attack. Метод должен рассчитать свое новое здоровье и вернуть True, если остался жив.
    def take_strike(self, attack):
        pass

    def get_health(self):
        pass

    def is_alive(self):
        return self.get_health() > 0

    def get_protection(self):
        pass

    def get_country(self):
        pass

    # Обновляет параметры перед новой битвой. Такие как, например, здоровье.
    def reset_battle_parameters(self):
        pass
