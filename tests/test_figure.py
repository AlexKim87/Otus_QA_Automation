import os
import inspect
from src.Figure import Figure
from src.Triangle import Triangle
from src.Circle import Circle


def test_square_in_src_folder_name():
    expected_path = '/Users/leningrad/Documents/Projects/Otus/Otus_QA_Automation/src/Figure.py'
    actual_path = os.path.abspath(inspect.getfile(Figure))
    assert actual_path == expected_path


def test_figure_has_name_attr(figure):
    if hasattr(figure, 'name'):  # в видеопримере название атрибута было без кавычек
        del figure
    else:
        raise ValueError("The Figure object doesn't have 'name' attribute")


def test_figure_has_addarea_method(figure):
    if not hasattr(figure, 'add_area'):
        raise NotImplemented("get_area method not implemented")


def test_figure_addarea_method():
    circle = Circle()
    triangle = Triangle()
    circle.radius = 5
    triangle.side1, triangle.side2, triangle.side3 = 5, 6, 7
    circle_area = circle.get_area
    triangle_area = triangle.get_area
    assert circle_area+triangle_area == circle.add_area(triangle)

