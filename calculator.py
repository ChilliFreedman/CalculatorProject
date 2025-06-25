from abc import ABC, abstractmethod

class Shap(ABC):
    @abstractmethod
    def get_area(self):
        pass

    def __str__(self):
        return f"shap: {self.__class__.__name__}:: area: {self.get_area()} square meters."

    # @abstractmethod
    # def get_perimeter(self):
    #     pass


