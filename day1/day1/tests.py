from io import StringIO
from . import parse_input
from . import required_fuel
from . import total_fuel


def test_read_input():
    lines = "\n".join(("88062", "147838", "73346"))
    assert list(parse_input(StringIO(lines))) == [88062, 147838, 73346]


def test_mass_12():
    assert required_fuel(12) == 2


def test_mass_14():
    assert required_fuel(14) == 2


def test_mass_1969():
    assert required_fuel(1969) == 654


def test_mass_100756():
    assert required_fuel(100756) == 33583


def test_total_fuel_14():
    assert total_fuel(14) == 2


def test_total_fuel_1969():
    assert total_fuel(1969) == 966


def test_total_fuel_100756():
    assert total_fuel(100756) == 50346
