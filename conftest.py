import pytest
from src.Circle import Circle
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture(scope='session')
def circle():
    circle = Circle()

    yield circle

    del circle


@pytest.fixture(scope='session')
def figure():
    figure = Figure()

    yield figure

    del figure


@pytest.fixture(scope='session')
def rectangle():
    rectangle = Rectangle()

    yield rectangle

    del rectangle


@pytest.fixture(scope='session')
def square():
    square = Square()

    yield square

    del square


@pytest.fixture(scope='session')
def triangle():
    triangle = Triangle()

    yield triangle

    del triangle

