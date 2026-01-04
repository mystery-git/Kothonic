from kothonic.stdlib.exceptions.illegal_state_exception import IllegalStateException


def test_illegal_state_exception_instantiation():
	"""Test that IllegalStateException can be instantiated."""
	exc = IllegalStateException("Something went wrong")
	assert isinstance(exc, IllegalStateException)
	assert isinstance(exc, Exception)
	assert str(exc) == "Something went wrong"


def test_illegal_state_exception_inheritance():
	"""Test inheritance hierarchy."""
	assert issubclass(IllegalStateException, Exception)


def test_illegal_state_exception_empty():
	"""Test instantiation without arguments (if supported by base Exception)."""
	exc = IllegalStateException()
	assert isinstance(exc, IllegalStateException)
