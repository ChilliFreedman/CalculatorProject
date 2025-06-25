from math import pi
from calculator import Shap
class Circle(Shap):
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
      return  2 * pi * self.radius


ci = Circle(5)
print(ci)