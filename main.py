from calculator import Shap
from circle import Circle
from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle


def printer_shap(shep: Shap):
    print(shep)

printer_shap(Rectangle(5,10))
printer_shap(Square(5))
printer_shap(Triangle(8,4))
printer_shap(Circle(4))
printer_shap(Hexagon(3))
