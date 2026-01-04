import pytest

from kothonic.stdlib.types.char import Char


def test_char_creation():
	c = Char("a")
	assert c == "a"


def test_char_comparison():
	c1 = Char("a")
	c2 = Char("a")
	c3 = Char("b")
	assert c1 == c2
	assert c1 < c3


if __name__ == "__main__":
	pytest.main([__file__])
