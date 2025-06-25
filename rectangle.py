from calculator import Shap

class Rectangle(Shap):
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return self.length * 2 + self.width * 2

# re = Rectangle(5,10)
# print(re)
