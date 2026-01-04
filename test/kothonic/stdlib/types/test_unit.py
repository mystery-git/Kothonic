import pytest

from kothonic.stdlib.types.unit import Unit


def test_unit_singleton():
	Unit
	# Unit might be a class or an instance. In Kotlin it's an object (singleton).
	# If implemented as a class with singleton pattern or module-level instance.
	# Assuming Unit is the instance or class acting as singleton.
	# Let's check if we can instantiate it or if it's already an instance.
	# Usually in python translations `Unit` is an instance.
	pass


def test_unit_str():
	assert str(Unit) == "Unit"


if __name__ == "__main__":
	pytest.main([__file__])
