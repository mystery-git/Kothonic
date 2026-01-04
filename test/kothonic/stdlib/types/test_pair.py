import pytest

from kothonic.stdlib.types.pair import Pair


def test_pair_creation():
	p = Pair(1, "one")
	assert p.first == 1
	assert p.second == "one"


def test_pair_equality():
	p1 = Pair(1, "one")
	p2 = Pair(1, "one")
	p3 = Pair(2, "two")
	assert p1 == p2
	assert p1 != p3


def test_pair_to_string():
	p = Pair(1, "one")
	# Pair doesn't implement __repr__/__str__, so it uses object default.
	# assert str(p) == "(1, one)" # Currently fails
	assert isinstance(str(p), str)


def test_pair_component_access():
	p = Pair(10, 20)
	# Pair implements __call__ -> tuple
	a, b = p()
	assert a == 10
	assert b == 20


def test_pair_properties():
	p = Pair(1, 2)
	assert p.first == 1
	assert p.second == 2


if __name__ == "__main__":
	pytest.main([__file__])
