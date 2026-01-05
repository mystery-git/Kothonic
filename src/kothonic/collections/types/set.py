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

	# Kotlin: infix fun <T> Iterable<T>.union(other: Iterable<T>): Set<T>
	@override
	def union(self, other: ABCIterable[T]) -> Set[T]:  # type: ignore
		"""
		Returns a set containing all distinct elements from both collections.
		"""
		return Set(super().union(other))

	# Kotlin: infix fun <T> Iterable<T>.intersect(other: Iterable<T>): Set<T>
	@override
	def intersect(self, other: ABCIterable[T]) -> Set[T]:
		"""
		Returns a set containing all elements that are contained by both this collection and the specified collection.
		"""
		return Set(self.intersection(other))

	# Kotlin: infix fun <T> Iterable<T>.subtract(other: Iterable<T>): Set<T>
	@override
	def subtract(self, other: ABCIterable[T]) -> Set[T]:
		"""
		Returns a set containing all elements that are contained by this collection and not contained by the specified collection.
		"""
		return Set(self.difference(other))
