from src.core.data.models.value_objects import technology
import value_objects as vObjects


class JobModel:
    vacancy_id: str
    provider: vObjects.Provider
    url: str
    location: str
    description: str
    is_remote: bool
    technicalLevel: vObjects.TechnicalLevel
    type: vObjects.Type
    cltPj: vObjects.Hiring_regime
    salary: float
    salary_pj: float
    company_name: str
    company_description: str
    company_size: vObjects.Company_size
    company_ocupation_area: str
    benefit: list[vObjects.Benefit]
    technology: list[vObjects.technology]

    def __init__(self,
                 vacancy_id: str,
                 provider: vObjects.Provider,
                 url: str,
                 location: str,
                 description: str,
                 is_remote: bool,
                 technicalLevel: vObjects.TechnicalLevel,
                 type: vObjects.Type,
                 cltPj: vObjects.Hiring_regime,
                 salary: float,
                 salary_pj: float,
                 company_name: str,
                 company_description: str,
                 company_size: vObjects.Company_size,
                 company_ocupation_area: str,
                 benefit: list[vObjects.Benefit],
                 technology: list[vObjects.technology],
                 ):

        self.vacancy_id = vacancy_id
        self.provider = provider
        self.url = url
        self.location = location
        self.description = description
        self.is_remote = is_remote
        self.technicalLevel = technicalLevel
        self.type = type
        self.cltPj = cltPj
        self.salary = salary
        self.salary_pj = salary_pj
        self.company_name = company_name
        self.company_description = company_description
        self.company_size = company_size
        self.company_ocupation_area = company_ocupation_area
        self.technicalLevel = technicalLevel
        self.benefit = benefit
        self.technology = technology

    def fromDict(map: dict):
        return JobModel(
            vacancy_id=map["vacancy_id"],
            provider=map['provider'],
            url=map['url'],
            location=map['location'],
            description=map['description'],
            is_remote=map['is_remote'],
            technicalLevel=map['technicalLevel'],
            type=map['type'],
            cltPj=map['cltPj'],
            salary=map['salary'],
            salary_pj=map['salary_pj'],
            company_name=map['company_name'],
            company_description=map['company_description'],
            company_size=map['company_size'],
            company_ocupation_area=map['company_ocupation_area'],
            benefit=vObjects.benefitsFromList(map['benefit']),
            technology=vObjects.technologiesFromList(map['technology'])
            )
