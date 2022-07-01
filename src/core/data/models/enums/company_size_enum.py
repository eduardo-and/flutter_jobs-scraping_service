from enum import Enum


class CompanySizeEnum(Enum):
    UNDEFINED = 0
    PEQUENA = 1
    MEDIA = 2
    GRANDE = 3

    def fromName(name: str):
        if name == "pequena":
            return CompanySizeEnum.PEQUENA
        elif name == "media":
            return CompanySizeEnum.MEDIA
        elif name == "grande":
            return CompanySizeEnum.GRANDE
        else:
            return CompanySizeEnum.UNDEFINED

    def fromNumber(number: int):
        if number == 1:
            return CompanySizeEnum.PEQUENA
        elif number == 2:
            return CompanySizeEnum.MEDIA
        elif number == 3:
            return CompanySizeEnum.GRANDE
        else:
            return CompanySizeEnum.UNDEFINED
