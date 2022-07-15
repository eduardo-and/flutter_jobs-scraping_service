from abc import ABC, abstractmethod
import traceback


class FJobsException(Exception, ABC):
    details: str
    traceback: traceback

    @abstractmethod
    def __init__(self, message, details="", traceback=""):
        self.details = details
        self.traceback = traceback
        super().__init__(message)

    @abstractmethod
    def lauchLog():
        pass


class InvalidVacancyException(Exception):

    def __init__(self, message, details="", traceback=""):
        super().__init__(message,details,traceback)

    def lauchLog(self):
        pass
