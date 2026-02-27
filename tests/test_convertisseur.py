import sys
import os
import pytest
import math

# Permet d'importer depuis src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from convertisseur import (
    celsius_vers_fahrenheit,
    fahrenheit_vers_celsius,
    celsius_vers_kelvin,
    kelvin_vers_celsius,
)


def test_celsius_vers_fahrenheit():
    assert celsius_vers_fahrenheit(0) == 32.0
    assert celsius_vers_fahrenheit(100) == 212.0


def test_fahrenheit_vers_celsius():
    assert fahrenheit_vers_celsius(32) == 0.0
    assert fahrenheit_vers_celsius(212) == 100.0


def test_celsius_vers_kelvin():
    assert celsius_vers_kelvin(0) == 273.15


def test_kelvin_vers_celsius():
    assert kelvin_vers_celsius(273.15) == 0.0


def test_kelvin_negatif():
    with pytest.raises(ValueError):
        kelvin_vers_celsius(-5)


def test_round_trip():
    c = 37
    k = celsius_vers_kelvin(c)
    c_back = kelvin_vers_celsius(k)
    assert math.isclose(c_back, c, rel_tol=1e-9)