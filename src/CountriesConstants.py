class CountryConstants:
    ID = None
    FLAG = None
    MARCH = None

    def __init__(self, id, flag, march):
        self.ID = id
        self.FLAG = flag
        self.MARCH = march


GREAT_BRITAIN = CountryConstants(1, "🇬🇧", "For the Queen!!!")
FRANCE = CountryConstants(2, "🇫🇷", "Crush the Bastille!")
