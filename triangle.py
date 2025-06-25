from rectangle import Rectangle
from math import sqrt
class Triangle(Rectangle):
    def __init__(self,length, width):
        super().__init__(length, width)
        self.diagonal = None

    def get_area(self):
        return super().get_area() / 2

    def get_perimeter(self):
        self.diagonal = sqrt(self.length ** 2 + self.width ** 2)
        return self.length + self.width + self.diagonal

# tr = Triangle(10,5)
# print(tr)