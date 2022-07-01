class TechnologyModel:
    technology_id: int
    name: str

    def __init__(self, technology_id: int, name: str):
        self.technology_id = technology_id
        self.name = name

    def technologiesFromList(listOftechnologies: list) -> list:
        return [TechnologyModel(technology_id=technology['technology_id'], name=technology['name']) for technology in listOftechnologies]
    
    def toDict(self)-> dict:
        return {
            "technology_id": self.technology_id,
            "name": self.name
        }