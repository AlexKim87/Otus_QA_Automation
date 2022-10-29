from src.Figure import Figure


class Square(Figure):

    def __init__(self, name='Square', side1=1):
        super().__init__(name)
        self.side1 = side1

    @property
    def get_area(self):
        return self.side1**2

    @property
    def get_perimeter(self):
        return self.side1*4













