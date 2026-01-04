from typing import Any
from collections.abc import Callable

from kothonic.stdlib.types.function import Function


def test_function_type():
	"""Test that Function is an alias for Callable[..., Any]."""
	assert Function == Callable[..., Any]
	# Parameterized generics cannot be used with isinstance.
