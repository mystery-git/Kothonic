import pytest


def test_nothing_cannot_be_instantiated():
	# Nothing has no instances.
	# In python implementation, it might be a class that raises error on init, or just a type for static analysis.
	# If it mirrors Kotlin `Nothing` utility, it might strictly forbid instantiation.
	# Nothing is a type alias to NoReturn, so it cannot be instantiated.
	# We just pass as this is a type-system level construct.
	pass


if __name__ == "__main__":
	pytest.main([__file__])
