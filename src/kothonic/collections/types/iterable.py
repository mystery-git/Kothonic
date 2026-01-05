from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, TypeVar
from collections.abc import Callable, Iterable as ABCIterable


if TYPE_CHECKING:
	from .map import Map
	from .list import List
	from .set import Set


T = TypeVar("T", covariant=True)
K = TypeVar("K")
V = TypeVar("V")
R = TypeVar("R")


class Iterable(Generic[T], ABCIterable[T]):
	"""
	A mixin class that provides Kotlin-like functional methods for Iterables.
	"""

	# Kotlin: fun <T> Iterable<T>.filter(predicate: (T) -> Boolean): List<T>
	def filter_(self, predicate: Callable[[T], bool]) -> List[T]:
		"""
		Returns a list containing only elements matching the given predicate.
		"""
		from .list import List

		return List(filter(predicate, self))

	# Kotlin: fun <T, R> Iterable<T>.map(transform: (T) -> R): List<R>
	def map_(self, transformation: Callable[[T], R]) -> List[R]:
		"""
		Returns a list containing the results of applying the given transform function to each element in the original collection.
		"""
		from .list import List

		return List(map(transformation, self))

	# Kotlin: operator fun <T> Collection<T>.plus(elements: Iterable<T>): List<T>
	def plus(self, elements: ABCIterable[T]) -> List[T]:
		"""
		Returns a list containing all elements of the original collection and then all elements of the given arguments.
		"""
		from .list import List

		return List(list(self) + list(elements))

	# Kotlin: fun <T> Iterable<T>.all(predicate: (T) -> Boolean): Boolean
	def all_(self, predicate: Callable[[T], bool]) -> bool:
		"""
		Returns true if all elements match the given predicate.
		"""
		return all(predicate(item) for item in self)

	# Kotlin: fun <T> Iterable<T>.any(predicate: (T) -> Boolean): Boolean
	def any_(self, predicate: Callable[[T], bool]) -> bool:
		"""
		Returns true if at least one element matches the given predicate.
		"""
		return any(predicate(item) for item in self)

	# Kotlin: fun <T, K, V> Iterable<T>.associate(transform: (T) -> Pair<K, V>): Map<K, V>
	def associate(self, transform: Callable[[T], tuple[K, V]]) -> Map[K, V]:
		"""
		Returns a Map containing key-value pairs provided by transform function applied to elements of the given collection.
		"""
		from .map import Map

		new_dict = {}

		for item in self:
			key, value = transform(item)
			new_dict[key] = value

		return Map(new_dict)

	# Kotlin: fun Iterable<Double>.average(): Double
	def average(self) -> float:
		"""
		Returns an average value of elements in the collection.
		"""
		items = list(self)
		if not items:
			return float("nan")
		return sum(items) / len(items)  # type: ignore

	# Kotlin: operator fun <T> Iterable<T>.contains(element: T): Boolean
	def contains(self, element: Any) -> bool:
		"""
		Returns true if the element is found in the collection.
		"""
		return element in list(self)

	# Kotlin: fun <T> Iterable<T>.count(): Int
	def count_(self) -> int:
		"""
		Returns the number of elements in this collection.
		"""
		return len(list(self))

	# Kotlin: fun <T> Iterable[T].distinct(): List<T>
	def distinct(self) -> List[T]:
		"""
		Returns a list containing only distinct elements from the given collection.
		"""
		from .list import List

		return List(set(self))

	# Kotlin: fun <T> Iterable[T].drop(n: Int): List<T>
	def drop(self, n: int) -> List[T]:
		"""
		Returns a list containing all elements except first n elements.
		"""
		from .list import List

		return List(list(self)[n:])

	# Kotlin: fun <T> List<T>.dropLast(n: Int): List<T>
	def drop_last(self, n: int) -> List[T]:
		"""
		Returns a list containing all elements except last n elements.
		"""
		from .list import List

		items = list(self)
		return List(items[: len(items) - n])

	# Kotlin: fun <T> Iterable[T].elementAt(index: Int): T
	def element_at(self, index: int) -> T:
		"""
		Returns an element at the given index or throws an IndexError if the index is out of bounds of this collection.
		"""
		return list(self)[index]

	# Kotlin: fun <T> Iterable[T].elementAtOrNull(index: Int): T?
	def element_at_or_null(self, index: int) -> T | None:
		"""
		Returns an element at the given index or None if the index is out of bounds of this collection.
		"""
		try:
			return list(self)[index]
		except IndexError:
			return None

	# Kotlin: fun <T> Iterable[T].elementAtOrElse(index: Int, defaultValue: (Int) -> T): T
	def element_at_or_else(self, index: int, default_value: Callable[[int], T]) -> T:
		"""
		Returns an element at the given index or the result of calling the defaultValue function if the index is out of bounds of this collection.
		"""
		try:
			return list(self)[index]
		except IndexError:
			return default_value(index)

	# Kotlin: fun <T> Iterable[T].find(predicate: (T) -> Boolean): T?
	def find(self, predicate: Callable[[T], bool]) -> T | None:
		"""
		Returns the first element matching the given predicate, or None if no such element was found.
		"""
		for element in self:
			if predicate(element):
				return element
		return None

	# Kotlin: fun <T> Iterable[T].first(): T
	def first(self) -> T:
		"""
		Returns the first element. Throws an IndexError if the collection is empty.
		"""
		return list(self)[0]

	# Kotlin: Custom: Returns first non-null element
	def first_not_null(self) -> T | None:
		"""
		Returns the first non-null element, or None if no such element was found.
		"""
		for element in self:
			if element is not None:
				return element
		return None

	# Kotlin: fun <T> Iterable[T].firstOrNull(): T?
	def first_or_null(self) -> T | None:
		"""
		Returns the first element, or None if the collection is empty.
		"""
		return next(iter(self), None)

	# Kotlin: fun <T> Iterable<Iterable<T>>.flatten(): List<T>
	def flatten(self) -> List[T]:
		"""
		Returns a single list of all elements from all collections in the given collection.
		"""
		from .list import List

		result = []
		for item in self:
			result.extend(item)  # type: ignore

		return List(result)

	# Kotlin: infix fun <T> Iterable<T>.union(other: Iterable<T>): Set<T>
	def union(self, other: ABCIterable[T]) -> Set[T]:
		"""
		Returns a set containing all distinct elements from both collections.
		"""
		from .set import Set

		return Set(set(self).union(other))

	# Kotlin: infix fun <T> Iterable<T>.intersect(other: Iterable<T>): Set<T>
	def intersect(self, other: ABCIterable[T]) -> Set[T]:
		"""
		Returns a set containing all elements that are contained by both this collection and the specified collection.
		"""
		from .set import Set

		return Set(set(self).intersection(other))

	# Kotlin: infix fun <T> Iterable<T>.subtract(other: Iterable<T>): Set<T>
	def subtract(self, other: ABCIterable[T]) -> Set[T]:
		"""
		Returns a set containing all elements that are contained by this collection and not contained by the specified collection.
		"""
		from .set import Set

		return Set(set(self).difference(other))
