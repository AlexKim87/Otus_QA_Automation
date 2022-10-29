from src.Figure import Figure
from math import sqrt


class Triangle(Figure):

    def __init__(self, name='Triangle', side1=1, side2=1, side3=1):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if (self.side1+self.side2) < self.side3:
            raise ValueError("The length of a one side can't be less than a sum of 2 other sides")
        if (self.side1+self.side3) < self.side2:
            raise ValueError("The length of a one side can't be less than a sum of 2 other sides")
        if (self.side2+self.side3) < self.side1:
            raise ValueError("The length of a one side can't be less than a sum of 2 other sides")

    @property
    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    @property
    def get_area(self):
        p = self.get_perimeter/2  # This is 1/2 of the perimeter
        area = sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
        return area
