from enum import Enum


class TechnicalLevelEnum(Enum):
    UNDEFINED = 0
    JUNIOR = 1
    PLENO = 2
    SENIOR = 3

    def fromName(name: str):
        if name == "junior":
            return TechnicalLevelEnum.JUNIOR
        elif name == "pleno":
            return TechnicalLevelEnum.PLENO
        elif name == "senior":
            return TechnicalLevelEnum.SENIOR
        else:
            return TechnicalLevelEnum.UNDEFINED

    def fromNumber(number: int):
        if number == 1:
            return TechnicalLevelEnum.JUNIOR
        elif number == 2:
            return TechnicalLevelEnum.PLENO
        elif number == 3:
            return TechnicalLevelEnum.SENIOR
        else:
            return TechnicalLevelEnum.UNDEFINED
