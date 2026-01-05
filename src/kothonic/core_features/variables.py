from typing import TypeVar

from .inline_value import InlineValue
from .kotlin_value import KotlinValue


T = TypeVar("T")


class var(InlineValue[T], KotlinValue[T]):  # noqa: N801
	"""
	Represents a mutable variable in Kotlin.
	In Kothonic, this is a wrapper around a value that supports Kotlin-like operations.
	"""

	pass


class val(InlineValue[T], KotlinValue[T]):  # noqa: N801
	"""
	Represents a read-only (immutable) variable in Kotlin.
	In Kothonic, this functions similarly to 'var' but is intended to denote immutability semantics.
	"""

	pass
