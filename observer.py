from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, stock: str, price: float):
        pass
