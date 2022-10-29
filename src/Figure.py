class Figure:
    def __init__(self, name='Figure'):
        self.name = name

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('The parameter must be an instance of the Figure class')
        else:
            a = self.get_area
            b = figure.get_area
        return a+b


