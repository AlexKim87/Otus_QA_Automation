import os
import inspect
from src.Square import Square
from src.Figure import Figure


class Circle(Figure):

    PI = 3.14

    def __init__(self, name='Circle', radius=1):
        super().__init__(name)
        self.radius = radius

    @property
    def get_area(self):
        return(Circle.PI * self.radius)**2

    @property
    def get_circumference(self):
        return 2 * Circle.PI * self.radius

