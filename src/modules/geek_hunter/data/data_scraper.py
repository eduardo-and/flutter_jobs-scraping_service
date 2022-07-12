
from datetime import date
from bs4 import ResultSet, BeautifulSoup as soup

import requests as requests

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
            vacancyLink = vacancie.h2.a["href"]
            vacancies = self.__getVacancy(vacancyLink)

        return vacancies

    def __getVacancy(self, pageUrl: str) -> dict:
        vacancy = dict()

        htmlPage = requests.get(GEEK_HUNTER_BASE_URL + pageUrl)
        bSoup = soup(htmlPage.text, 'html.parser')
        vacancy["name"] = bSoup.findAll(
            "div", attrs={"class": "chakra-container"})[0].h1.text
        
        # __validateVacancy


    def __validateVacancy(self,title, description)->bool:
        return
    # Verifica se a vaga realmente é de flutter, buscando palavras chave no titulo e descrição