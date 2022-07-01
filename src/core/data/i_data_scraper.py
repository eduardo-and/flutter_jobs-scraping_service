
from abc import ABC, abstractmethod

class IDataScraper(ABC):
    
    @abstractmethod
    def run(self)->dict:
        pass
    
    