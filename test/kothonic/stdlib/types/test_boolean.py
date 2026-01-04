from kothonic.stdlib.types.boolean import Boolean


def test_boolean_type():
	"""Test that Boolean is an alias for bool."""
	assert Boolean is bool
	assert isinstance(True, Boolean)
	assert isinstance(False, Boolean)

	b: Boolean = True
	assert b is True


def test_boolean_operations():
	"""Test standard boolean operations."""
	t: Boolean = True
	f: Boolean = False

	assert t and t
	assert not (t and f)
	assert t or f
	assert not f
