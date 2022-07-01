from enum import Enum


class ProviderEnum(Enum):
    UNDEFINED = 0
    GEEKHUNTER = 1
    LINKEDIN = 2
    PROGRAMATHOR = 3

    def fromNumber(number: int):
        if number == 1:
            return ProviderEnum.GEEKHUNTER
        elif number == 2:
            return ProviderEnum.LINKEDIN
        elif number == 3:
            return ProviderEnum.PROGRAMATHOR
        else:
            return ProviderEnum.UNDEFINED
