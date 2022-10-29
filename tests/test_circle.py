import os
import inspect
from src.Circle import Circle
from src.Rectangle import Rectangle


def test_circle_in_src_folder_name():
    expected_path = '/Users/leningrad/Documents/Projects/Otus/Otus_QA_Automation/src/Circle.py'
    actual_path = os.path.abspath(inspect.getfile(Circle))
    assert actual_path == expected_path


def test_circle_has_name_attr(circle):
    if hasattr(circle, 'name'):  # в видеопримере название атрибута было без кавычек
        pass
    else:
        raise ValueError("The Circle object doesn't have 'name' attribute")


def test_circle_has_area_method(circle):
    if not hasattr(circle, 'get_area'):
        raise NotImplemented("get_area method not implemented")


def test_circle_area_method(circle):
    circle.radius = 3
    assert circle.get_area == 88.7364


def test_circle_has_circumference_method(circle):
    if not hasattr(circle, 'get_circumference'):
        raise NotImplemented("get_circumference method not implemented")


def test_circle_circumference_method(circle):
    circle.radius = 3
    assert circle.get_circumference == 18.84


def test_circle_has_addarea_method(circle):
    if not hasattr(circle, 'add_area'):
        raise NotImplemented("add_area method not implemented")


def test_circle_addarea_method(circle):
    rectangle = Rectangle()
    rectangle.side1, rectangle.side2 = 4.4, 4
    circle.radius = 5
    rectangle_area = rectangle.get_area
    circle_area = circle.get_area
    assert rectangle_area+circle_area == circle.add_area(rectangle)

