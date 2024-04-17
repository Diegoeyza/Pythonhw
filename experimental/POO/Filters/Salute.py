from abc import ABC, abstractmethod

class Salute(ABC):
    @abstractmethod
    def saludar(self):
        ...