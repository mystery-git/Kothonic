from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic, TypeVar
from collections.abc import Callable, Iterable as ABCIterable


if TYPE_CHECKING:
	from .map import Map
	from .list import List


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
		from .list import List

		return List(filter(predicate, self))

	# Kotlin: fun <T, R> Iterable<T>.map(transform: (T) -> R): List<R>
	def map_(self, transformation: Callable[[T], R]) -> List[R]:
		from .list import List

		return List(map(transformation, self))

	# Kotlin: operator fun <T> Collection<T>.plus(elements: Iterable<T>): List<T>
	def plus(self, elements: ABCIterable[T]) -> List[T]:
		from .list import List

		return List(list(self) + list(elements))

	# Kotlin: fun <T> Iterable<T>.all(predicate: (T) -> Boolean): Boolean
	def all_(self, predicate: Callable[[T], bool]) -> bool:
		return all(predicate(item) for item in self)

	# Kotlin: fun <T> Iterable<T>.any(predicate: (T) -> Boolean): Boolean
	def any_(self, predicate: Callable[[T], bool]) -> bool:
		return any(predicate(item) for item in self)

	# Kotlin: fun <T, K, V> Iterable<T>.associate(transform: (T) -> Pair<K, V>): Map<K, V>
	def associate(self, transform: Callable[[T], tuple[K, V]]) -> Map[K, V]:
		from .map import Map

		new_dict = {}

		for item in self:
			key, value = transform(item)
			new_dict[key] = value

		return Map(new_dict)

	# Kotlin: fun Iterable<Double>.average(): Double
	def average(self) -> float:
		items = list(self)
		if not items:
			return float("nan")
		return sum(items) / len(items)  # type: ignore

	# Kotlin: operator fun <T> Iterable<T>.contains(element: T): Boolean
	def contains(self, element: Any) -> bool:
		return element in list(self)

	# Kotlin: fun <T> Iterable<T>.count(): Int
	def count_(self) -> int:
		return len(list(self))

	# Kotlin: fun <T> Iterable[T].distinct(): List<T>
	def distinct(self) -> List[T]:
		from .list import List

		return List(set(self))

	# Kotlin: fun <T> Iterable[T].drop(n: Int): List<T>
	def drop(self, n: int) -> List[T]:
		from .list import List

		return List(list(self)[n:])

	# Kotlin: fun <T> List<T>.dropLast(n: Int): List<T>
	def drop_last(self, n: int) -> List[T]:
		from .list import List

		items = list(self)
		return List(items[: len(items) - n])

	# Kotlin: fun <T> Iterable[T].elementAt(index: Int): T
	def element_at(self, index: int) -> T:
		return list(self)[index]

	# Kotlin: fun <T> Iterable[T].elementAtOrNull(index: Int): T?
	def element_at_or_null(self, index: int) -> T | None:
		try:
			return list(self)[index]
		except IndexError:
			return None

	# Kotlin: fun <T> Iterable[T].elementAtOrElse(index: Int, defaultValue: (Int) -> T): T
	def element_at_or_else(self, index: int, default_value: Callable[[int], T]) -> T:
		try:
			return list(self)[index]
		except IndexError:
			return default_value(index)

	# Kotlin: fun <T> Iterable[T].find(predicate: (T) -> Boolean): T?
	def find(self, predicate: Callable[[T], bool]) -> T | None:
		for element in self:
			if predicate(element):
				return element
		return None

	# Kotlin: fun <T> Iterable[T].first(): T
	def first(self) -> T:
		return list(self)[0]

	# Kotlin: Custom: Returns first non-null element
	def first_not_null(self) -> T | None:
		for element in self:
			if element is not None:
				return element
		return None

	# Kotlin: fun <T> Iterable[T].firstOrNull(): T?
	def first_or_null(self) -> T | None:
		return next(iter(self), None)

	# Kotlin: fun <T> Iterable[Iterable<T>>.flatten(): List<T>
	def flatten(self) -> List[T]:
		from .list import List

		result = []
		for item in self:
			result.extend(item)  # type: ignore

		return List(result)
