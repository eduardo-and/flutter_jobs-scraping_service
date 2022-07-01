
from abc import ABC, abstractmethod


class IProcessor(ABC):

    @abstractmethod
    def __init__(self, data: list[dict]) -> None:
        pass

    @abstractmethod
    def run(self) -> dict:
        pass
