from __future__ import annotations

from typing import Generic, TypeVar, override
from collections.abc import Iterable as ABCIterable

from kothonic.core_features import KotlinValue

from .collection import Collection


T = TypeVar("T")


class Set(Generic[T], set[T], Collection[T], KotlinValue[set[T]]):
	"""
	A Kotlin-style set that extends Python's built-in set with additional functional methods.

	This class provides Kotlin-like operations such as filter_(), map_(), distinct(), and more, while maintaining full compatibility with Python's standard set type.
	"""

	# Kotlin: operator fun <T> Set<T>.plus(element: T): Set<T>
	# Kotlin: operator fun <T> Set<T>.plus(elements: Iterable<T>): Set<T>
	@override
	def plus(self, elements: ABCIterable[T] | T) -> Set[T]:  # type: ignore
		"""
		Returns a set containing all elements of the original set and then the given element or elements.
		"""
		new_set = self.copy()
		if isinstance(elements, ABCIterable) and not isinstance(elements, (str, bytes)):
			new_set.update(elements)
		else:
			new_set.add(elements)  # type: ignore
		return Set(new_set)
