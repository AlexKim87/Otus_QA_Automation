import os
import inspect
from src.Square import Square
from src.Circle import Circle


def test_square_in_src_folder_name():
    expected_path = '/Users/leningrad/Documents/Projects/Otus/Otus_QA_Automation/src/Square.py'
    actual_path = os.path.abspath(inspect.getfile(Square))
    assert actual_path == expected_path


def test_square_has_name_attr(square):
    if hasattr(square, 'name'): # в видеопримере название атрибута было без кавычек
        del square
    else:
        raise ValueError("The Square object doesn't have 'name' attribute")


def test_square_has_area_method(square):
    if not hasattr(square, 'get_area'):
        raise NotImplemented("get_area method not implemented")


def test_square_area_method(square):
    square.side1 = 3
    assert square.get_area == 9
    del square


def test_square_has_perimeter_method(square):
    if not hasattr(square, 'get_perimeter'):
        raise NotImplemented("get_perimeter method not implemented")


def test_square_perimeter_method(square):
    square.side1 = 3
    assert square.get_perimeter == 12
    del square


def test_square_has_addarea_method(square):
    if not hasattr(square, 'add_area'):
        raise NotImplemented("add_area method not implemented")


def test_square_addarea_method(square):
    circle = Circle()
    square.side1 = 3
    circle.radius = 5
    square_area = square.get_area
    circle_area = circle.get_area
    assert square_area+circle_area == square.add_area(circle)







