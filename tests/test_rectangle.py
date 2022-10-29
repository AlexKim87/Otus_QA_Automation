import os
import inspect
from src.Circle import Circle
from src.Rectangle import Rectangle


def test_rectangle_in_src_folder_name():
    expected_path = '/Users/leningrad/Documents/Projects/Otus/Otus_QA_Automation/src/Rectangle.py'
    actual_path = os.path.abspath(inspect.getfile(Rectangle))
    assert actual_path == expected_path


def test_rectangle_has_name_attr(rectangle):
    if hasattr(rectangle, 'name'):  # в видеопримере название атрибута было без кавычек
        del rectangle
    else:
        raise ValueError("The Rectangle object doesn't have 'name' attribute")


def test_rectangle_has_area_method(rectangle):
    if not hasattr(rectangle, 'get_area'):
        raise NotImplemented("get_area method not implemented")


def test_rectangle_area_method(rectangle):
    rectangle.side1 = 3
    rectangle.side2 = 4
    assert rectangle.get_area == 12
    del rectangle


def test_rectangle_has_perimeter_method(rectangle):
    if not hasattr(rectangle, 'get_perimeter'):
        raise NotImplemented("get_perimeter method not implemented")


def test_rectangle_perimeter_method(rectangle):
    rectangle.side1 = 3
    rectangle.side2 = 5
    assert rectangle.get_perimeter == 16


def test_rectangle_has_addarea_method(rectangle):
    if not hasattr(rectangle, 'add_area'):
        raise NotImplemented("add_area method not implemented")


def test_square_addarea_method(rectangle):
    circle = Circle()
    rectangle.side1 = 3
    rectangle.side2 = 4.5
    circle.radius = 5
    square_area = rectangle.get_area
    circle_area = circle.get_area
    assert square_area+circle_area == rectangle.add_area(circle)

