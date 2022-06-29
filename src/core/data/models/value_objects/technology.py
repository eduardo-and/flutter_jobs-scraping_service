class Technology:
    technology_id: int
    name: str

    def __init__(self, technology_id: int, name: str):
        self.technology_id = technology_id
        self.name = name

    def technologiesFromList(listOftechnologies: list) -> list:
        return [Technology(technology_id=technology['benefit_id'], name=technology['name']) for technology in listOftechnologies]
