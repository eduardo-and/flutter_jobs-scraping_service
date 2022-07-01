class BenefitModel:
    benefit_id: int
    name: str

    def __init__(self, benefit_id: int, name: str):
        self.benefit_id = benefit_id
        self.name = name

    def benefitsFromList(listOfBenefits: list):
        return [BenefitModel(benefit_id=benefit['benefit_id'], name=benefit['name']) for benefit in listOfBenefits]

    def toDict(self)-> dict:
        return {
            "benefit_id": self.benefit_id,
            "name": self.name
        }
        
            
        