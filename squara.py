from rectangle import Rectangle

class Squara(Rectangle):

    def __init__(self,side):
        super().__init__(side, side)
        self.side = side


# sq = Squara(5)
# print(sq)

