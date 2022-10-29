import sys
from src.Square import Square


class Rectangle(Square):
    def __init__(self, name='Rectangle', side1=1, side2=1):
        super().__init__(name, side1)
        self.side2 = side2

    @property
    def get_perimeter(self):
        return (self.side1+self.side2)*2

    @property
    def get_area(self):
        return self.side1*self.side2



