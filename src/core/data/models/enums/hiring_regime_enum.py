from enum import Enum

class HiringRegimeEnum(Enum):
    UNDEFINED=0
    CLT=1
    PJ=2
    OPCIONAL=3
    
    def fromName(name: str):
        if name == "clt":
            return HiringRegimeEnum.CLT
        elif name == "pj":
            return HiringRegimeEnum.PJ
        elif name == "opcional":
            return HiringRegimeEnum.OPCIONAL
        else:
            return HiringRegimeEnum.UNDEFINED
    
    def fromNumber(number: int):
        if number == 1:
            return HiringRegimeEnum.CLT
        elif number == 2:
            return HiringRegimeEnum.PJ
        elif number == 3:
            return HiringRegimeEnum.OPCIONAL
        else:
            return HiringRegimeEnum.UNDEFINED