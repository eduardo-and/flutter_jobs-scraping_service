from enum import Enum


class TypeEnum(Enum):
    UNDEFINED = 0
    DESENVOLVEDOR = 1
    ANALISTA = 2
    TECHLEAD = 3

    def fromName(name: str):
        if name == "desenvolvedor":
            return TypeEnum.DESENVOLVEDOR
        elif name == "analista":
            return TypeEnum.ANALISTA
        elif name == "techlead":
            return TypeEnum.TECHLEAD
        else:
            return TypeEnum.UNDEFINED

    def fromNumber(number: int):
        if number == 1:
            return TypeEnum.DESENVOLVEDOR
        elif number == 3:
            return TypeEnum.ANALISTA
        elif number == 4:
            return TypeEnum.TECHLEAD
        else:
            return TypeEnum.UNDEFINED
