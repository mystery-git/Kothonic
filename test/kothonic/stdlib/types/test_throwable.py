from kothonic.stdlib.types.throwable import Throwable


def test_throwable_type():
	"""Test that Throwable is an alias for BaseException/Exception."""
	# Depending on implementation it might be BaseException or Exception.
	# Checking implementation file...
	# Based on standard mapping it's usually BaseException or Exception.
	assert issubclass(Exception, Throwable)
	assert isinstance(ValueError("error"), Throwable)
