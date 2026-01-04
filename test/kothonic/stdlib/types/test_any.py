from typing import Any as _Any

from kothonic.stdlib.types.any import Any


def test_any_type():
	"""Test that Any is an alias for typing.Any."""
	assert Any is _Any
	# Any cannot be used with isinstance in Python.

	# Note: In Kotlin Any does not include null, but in Python Any is object which includes everything.
	# The distinction is typically enforced by type checkers, not runtime constraints on 'object'.
