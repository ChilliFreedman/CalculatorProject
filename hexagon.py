from calculator import Shap
from math import sqrt
class Hexagon(Shap):
    def __init__(self,side):
        self.side = side

    def get_area(self):
        return 3 * sqrt(3) * self.side ** 2 / 2
# he = Hexagon(4)
# print(he)