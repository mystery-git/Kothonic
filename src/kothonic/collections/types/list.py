from typing import Generic, TypeVar

from kothonic.core_features import KotlinValue

from .collection import Collection


T = TypeVar("T")


class List(Generic[T], list[T], Collection[T], KotlinValue[list[T]]):
	"""
	A Kotlin-style list that extends Python's built-in list with additional functional methods.

	This class provides Kotlin-like operations such as filter_(), map_(), flatten(), distinct() and more, while maintaining full compatibility with Python's standard list type.
	"""

	pass
