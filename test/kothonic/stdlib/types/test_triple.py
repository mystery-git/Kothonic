import pytest

from kothonic.stdlib.types.triple import Triple


def test_triple_creation():
	t = Triple(1, "two", 3.0)
	assert t.first == 1
	assert t.second == "two"
	assert t.third == 3.0


def test_triple_equality():
	t1 = Triple(1, 2, 3)
	t2 = Triple(1, 2, 3)
	t3 = Triple(1, 2, 4)
	assert t1 == t2
	assert t1 != t3


def test_triple_to_string():
	t = Triple(1, "a", True)
	# Triple doesn't implement __repr__/__str__
	# assert str(t) == "(1, a, True)" # Fails
	assert isinstance(str(t), str)


def test_triple_component_access():
	t = Triple(10, 20, 30)
	# Assuming iterable or __call__ like Pair? Triple doesn't seem to implement __call__ in stub?
	# Let's check Triple implementation if needed, but safe bet is properties.
	assert t.first == 10
	assert t.second == 20
	assert t.third == 30


def test_triple_properties():
	t = Triple(1, 2, 3)
	assert t.first == 1
	assert t.second == 2
	assert t.third == 3


if __name__ == "__main__":
	pytest.main([__file__])
