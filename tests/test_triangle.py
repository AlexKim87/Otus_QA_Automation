import os
import inspect

import pytest

from src.Circle import Circle
from src.Triangle import Triangle


def test_triangle_in_src_folder_name():
    expected_path = '/Users/leningrad/Documents/Projects/Otus/Otus_QA_Automation/src/Triangle.py'
    actual_path = os.path.abspath(inspect.getfile(Triangle))
    assert actual_path == expected_path


def test_triangle_has_name_attr(triangle):
    if hasattr(triangle, 'name'):  # в видеопримере название атрибута было без кавычек
        del triangle
    else:
        raise ValueError("The Triangle object doesn't have 'name' attribute")


def test_triangle_check_sides_length():

    with pytest.raises(ValueError):
        Triangle(side1=1, side2=2, side3=10)


def test_triangle_has_area_method(triangle):
    if not hasattr(triangle, 'get_area'):
        raise NotImplemented("get_area method not implemented")


def test_triangle_area_method(triangle):
    triangle.side1 = 3
    triangle.side2 = 4
    triangle.side3 = 5
    assert triangle.get_area == 6


def test_triangle_has_perimeter_method(triangle):
    if not hasattr(triangle, 'get_perimeter'):
        raise NotImplemented("get_perimeter method not implemented")


def test_triangle_perimeter_method(triangle):
    triangle.side1 = 1
    triangle.side2 = 2
    triangle.side3 = 3.5
    assert triangle.get_perimeter == 6.5


def test_triangle_has_addarea_method(triangle):
    if not hasattr(triangle, 'add_area'):
        raise NotImplemented("add_area method not implemented")


def test_triangle_addarea_method(triangle):
    circle = Circle()
    triangle.side1, triangle.side2, triangle.side3 = 3, 4, 5
    circle.radius = 7
    triangle_area = triangle.get_area
    circle_area = circle.get_area
    assert triangle_area+circle_area == triangle.add_area(circle)



