import pytest

from kothonic.stdlib.types.enum_class.enum import Enum
from kothonic.stdlib.functions.enum_value_of import enum_value_of


class Color(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3


def test_enum_value_of_valid():
	"""Test retrieving a valid enum member."""
	assert enum_value_of(Color, "RED") == Color.RED
	assert enum_value_of(Color, "GREEN") == Color.GREEN


def test_enum_value_of_invalid():
	"""Test retrieving an invalid enum member raises KeyError."""
	with pytest.raises(KeyError):
		enum_value_of(Color, "YELLOW")


def test_enum_value_of_case_sensitive():
	"""Test that enum_value_of is case-sensitive."""
	with pytest.raises(KeyError):
		enum_value_of(Color, "red")


if __name__ == "__main__":
	pytest.main([__file__])

