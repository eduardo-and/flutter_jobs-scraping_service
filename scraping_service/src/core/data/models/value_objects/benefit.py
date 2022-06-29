class Benefit:
    benefit_id: int
    name: str

    def __init__(self, benefit_id: int, name: str):
        self.benefit_id = benefit_id
        self.name = name

    def benefitsFromList(listOfBenefits: list):
        return [Benefit(benefit_id=benefit['benefit_id'], name=benefit['name']) for benefit in listOfBenefits]
