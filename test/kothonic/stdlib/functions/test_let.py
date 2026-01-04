import pytest

from kothonic.stdlib import Int, String


def test_let_transform():
	val = Int(5)
	result = val.let(lambda x: x * 2)
	assert result == 10


def test_let_string():
	val = String("hello")
	result = val.let(lambda x: len(x))
	assert result == 5


def test_let_null_handling():
	pass
	# TODO: Implement let for None if possible or decide on behavior.


if __name__ == "__main__":
	pytest.main([__file__])
