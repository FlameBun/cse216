from abc import ABC, abstractmethod

class pyTPS_Transaction(ABC):
    @abstractmethod
    def doTransaction(self):
        pass

    @abstractmethod
    def undoTransaction(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
