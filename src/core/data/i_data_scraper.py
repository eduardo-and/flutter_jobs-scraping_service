
from abc import ABC, abstractmethod

class IDataScraper(ABC):
    
    @abstractmethod
    def run(self)->list[dict]:
        pass    
                
    def __getUrls(self) -> list:
        pass

    def __getData(self) -> dict:
        pass