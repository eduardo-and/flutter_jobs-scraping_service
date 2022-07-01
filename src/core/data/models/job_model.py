from value_objects import *
from enums import *


class JobModel:
    vacancy_id: str
    provider: ProviderEnum
    url: str
    location: str
    description: str
    is_remote: bool
    technicalLevel: TechnicalLevelEnum
    type: TypeEnum
    cltPj: HiringRegimeEnum
    salary: float
    salary_pj: float
    company_name: str
    company_description: str
    company_size: CompanySizeEnum
    company_ocupation_area: str
    benefit: list[BenefitModel]
    technology: list[TechnologyModel]

    def __init__(self,
                 vacancy_id: str,
                 provider: ProviderEnum,
                 url: str,
                 location: str,
                 description: str,
                 is_remote: bool,
                 technicalLevel: TechnicalLevelEnum,
                 type: TypeEnum,
                 cltPj: HiringRegimeEnum,
                 salary: float,
                 salary_pj: float,
                 company_name: str,
                 company_description: str,
                 company_size: CompanySizeEnum,
                 company_ocupation_area: str,
                 benefit: list[BenefitModel],
                 technology: list[TechnologyModel],
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
            # FIX ISTANCES
            vacancy_id=map["vacancy_id"],
            provider=ProviderEnum.fromNumber(map['provider']),
            url=map['url'],
            location=map['location'],
            description=map['description'],
            is_remote=map['is_remote'],
            technicalLevel=TechnicalLevelEnum.fromName(map['technicalLevel']),
            type=TypeEnum.fromName(map['type']),
            cltPj=HiringRegimeEnum.fromName(map['cltPj']),
            salary=map['salary'],
            salary_pj=map['salary_pj'],
            company_name=map['company_name'],
            company_description=map['company_description'],
            company_size=CompanySizeEnum.fromName(map['company_size']),
            company_ocupation_area=map['company_ocupation_area'],
            benefit=BenefitModel.benefitsFromList(map['benefit']),
            technology=TechnologyModel.technologiesFromList(
                map['technology'])
        )

    def toDict(self) -> dict:
        return{
            "vacancy_id": self.vacancy_id,
            "provider": self.provider.value,
            "url": self.url,
            "location": self.location,
            "description": self.description,
            "is_remote": self.is_remote,
            "technicalLevel": self.technicalLevel.value,
            "type": self.type.value,
            "cltPj": self.cltPj.value,
            "salary": self.salary,
            "salary_pj": self.salary_pj,
            "company_name": self.company_name,
            "company_description": self.company_description,
            "company_size": self.company_size.value,
            "company_ocupation_area": self.company_ocupation_area,
            "benefit": [ben.toDict() for ben in self.benefit],
            "technolog": [technology.toDict() for technology in self.technology]
        }

    def __eq__(self, other):
        return self.vacancy_id == other.vacancy_id and self.provider == other.provider and self.url == other.url and self.location == other.location and self.description == other.description and self.is_remote == other.is_remote and self.technicalLevel == other.technicalLevel and self.type == other.type and self.cltPj == other.cltPj and self.salary == other.salary and self.salary_pj == other.salary_pj and self.company_name == other.company_name and self.company_description == other.company_description and self.company_size == other.company_size and self.company_ocupation_area == other.company_ocupation_area and self.benefit == other.benefit and self.technology == other.technology




# dictjobModelMock = {
#     "vacancy_id": "vacancy_id",
#     "provider": 1,
#     "url": "url",
#     "location": "location",
#     "description": "description",
#     "is_remote": True,
#     "technicalLevel": "pleno",
#     "type": "desenvolvedor",
#     "cltPj": "pj",
#     "salary": 1512.0,
#     "salary_pj": 1550.0,
#     "company_name": "company_name",
#     "company_description": "company_description",
#     "company_size": "pequena",
#     "company_ocupation_area": "company_ocupation_area",
#     "benefit": [
#         {
#             "benefit_id": 1,
#             "name": "benefit_name"
#         }
#     ],
#     "technology": [
#         {
#             "technology_id": 1,
#             "name": "technology_name"
#         }
#     ]
# }

# job = JobModel.fromDict(dictjobModelMock)

# print(job)

# print(job.toDict())
