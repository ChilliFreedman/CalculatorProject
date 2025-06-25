from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self,side):
        super().__init__(side, side)
        self.side = side


# sq = Square(5)
# print(sq)

