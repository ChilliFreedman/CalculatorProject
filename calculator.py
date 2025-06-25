from abc import ABC, abstractmethod

class Shap(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __str__(self):
        return f"Shap name: {self.__class__.__name__}.\nArea: {self.get_area()} square meters.\nPerimeter: {self.get_perimeter() } meters."




