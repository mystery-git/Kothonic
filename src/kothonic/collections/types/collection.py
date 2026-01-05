from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar
from collections.abc import Iterable as ABCIterable, Collection as ABCCollection

from .iterable import Iterable


if TYPE_CHECKING:
	pass

T = TypeVar("T", covariant=True)


class Collection(Generic[T], Iterable[T], ABCCollection[T]):
	"""
	A mixin class that extends KotlinIterable with Collection-specific optimizations.
	"""

	# Kotlin: fun <T> Collection<T>.containsAll(elements: Collection<T>): Boolean
	def contains_all(self, elements: ABCIterable[T]) -> bool:
		"""
		Checks if all elements in the specified collection are contained in this collection.
		"""
		container = list(self)
		return all(element in container for element in elements)

	# Kotlin: fun <T> Collection<T>.count(): Int
	def count_(self) -> int:
		"""
		Returns the number of elements in this collection.
		"""
		return len(self)

	# Kotlin: fun <T> Collection<T>.isEmpty(): Boolean
	def is_empty(self) -> bool:
		"""
		Returns true if the collection is empty (contains no elements), false otherwise.
		"""
		return len(self) == 0

	# Kotlin: fun <T> Collection<T>.isNotEmpty(): Boolean
	def is_not_empty(self) -> bool:
		"""
		Returns true if the collection is not empty, false otherwise.
		"""
		return len(self) > 0

	# Kotlin: val Collection<T>.size: Int
	@property
	def size(self) -> int:
		"""
		Returns the size of the collection.
		"""
		return len(self)
