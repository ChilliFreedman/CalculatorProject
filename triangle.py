from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self,length, width):
        super().__init__(length, width)

    def get_area(self):
        return self.length * self.width / 2

# tr = Triangle(10,5)
# print(tr)