import pytest

from kothonic.random import Random


def test_random_next_int():
	# Assuming Random is an object or class with companion-like behavior or instance
	r = Random
	val = r.next_int()  # If default generates int
	assert isinstance(val, int)


if __name__ == "__main__":
	pytest.main([__file__])
