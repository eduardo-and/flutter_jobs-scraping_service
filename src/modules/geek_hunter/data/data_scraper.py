
from datetime import date
import requests as requests
from bs4 import ResultSet, BeautifulSoup as soup
from lxml import etree


from core import *


class GeekHunterDataScraper(IDataScraper):
    initTime: date
    paginationUrls: list
    jobs: list[dict]

    def run(self) -> list[dict]:
        job: dict
        self.initTime = date.today()
        self.paginationUrls = self.__getUrls()

        for paginationUrl in self.paginationUrls:

            jobsByPage = self.__getVacanciesFromPage(paginationUrl)
            self.jobs.append(jobsByPage)

        return self.jobs

    def __getUrls(self) -> list:
        elements: ResultSet
        urlList = []

        htmlPage = requests.get(GEEK_HUNTER_START_URL)
        bSoup = soup(htmlPage.text, 'html.parser')
        paginationSoup = bSoup.find_all("div", {"class": "pagination"})

        if(len(paginationSoup) == 0):
            urlList.append(GEEK_HUNTER_START_URL)
        else:
            aObjects = paginationSoup[0].find_all("a")
            for a in aObjects:
                urlList.append(a.get("href"))

        return urlList

    def __getVacanciesFromPage(self, pageUrl: str) -> list[dict]:
        vacancies = [dict]

        htmlPage = requests.get(pageUrl)
        bSoup = soup(htmlPage.text, 'html.parser')
        vacanciesSoup = bSoup.find_all(
            "div", attrs={"class": "information"})

        for vacancie in vacanciesSoup:
            try:
                vacancyLink = vacancie.h2.a["href"]
                vacancies.append(self.__getVacancy(vacancyLink))
            except InvalidVacancyException as error:
                error.lauchLog()  # Implement later
                continue

        return vacancies

    def __getVacancy(self, pageUrl: str) -> dict:
        vacancy = dict()

        htmlPage = requests.get(GEEK_HUNTER_BASE_URL + pageUrl)
        bSoup = soup(htmlPage.text, 'html.parser')
        vacancy["name"] = bSoup.findAll(
            "div", attrs={"class": "chakra-container"})[0].h1.text

        vacancy["description"] = self.__createDescription(bSoup)
        vacancy["name"] = vacancy["name"].replace('Flutter', '')
        if(not self.__validateVacancy(title=vacancy["name"], description=vacancy["description"])):
            raise InvalidVacancyException("Vacancy is not valid")

    def __validateVacancy(self, title, description) -> bool:

        # if("flutter" not in title.lower()):
        #     if("mobile" not in title.lower() and "flutter" not in description.lower()):
        #         return False
        return False

    def __createDescription(self, bSoup) -> str:
        description: str = ""
        dom = etree.HTML(str(bSoup))

        # Get Atividades
        description = dom.xpath(
            '//*[@id="__next"]/div[3]/div/div/div[1]/div[3]/div')[0].text
        if(description != "" and type(description) != None):
            description = description.replace('•\t', '')
            description = 'Atividades: ' + description
        return description
