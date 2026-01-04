from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar, override
from collections.abc import Callable, Iterable as ABCIterable

from kothonic.core_features import KotlinValue

from .collection import Collection


if TYPE_CHECKING:
	from .set import Set
	from .list import List


K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("T")
R = TypeVar("R")


class Map(Generic[K, V], dict[K, V], Collection[K], KotlinValue[dict[K, V]]):
	"""
	A Kotlin-style map that extends Python's built-in dict with additional functional methods.

	This class provides Kotlin-like operations such as contains_key(), contains_value(), filter_(), map_(), plus(), all_(), any_(), associate(), average(), and more, while maintaining full compatibility with Python's standard dict type.
	"""

	# Kotlin: fun <K, V> Map<K, V>.containsKey(key: K): Boolean
	def contains_key(self, key: K) -> bool:
		"""Returns true if the map contains the specified key."""
		return key in self.keys()

	# Kotlin: fun <K, V> Map<K, V>.containsValue(value: V): Boolean
	def contains_value(self, value: V) -> bool:
		"""Returns true if the map maps one or more keys to the specified value."""
		return value in self.values()

	# Kotlin: val Map<K, V>.entries: Set<Entry<K, V>>
	@property
	def entries(self) -> Set[tuple[K, V]]:
		from .set import Set

		return Set(self.items())

		# Kotlin: operator fun <K, V> Map<K, V>.plus(map: Map<out K, out V>): Map<K, V>

	def plus(self, other: dict[K, V] | ABCIterable[tuple[K, V]]) -> Map[K, V]:  # type: ignore[override]
		new_map = self.copy()
		if isinstance(other, dict):
			new_map.update(other)
		else:
			new_map.update(dict(other))
		return Map(new_map)

	# Kotlin: fun <K, V> Map<K, V>.filter(predicate: (Entry<K, V>) -> Boolean): Map<K, V>
	@override
	def filter_(self, predicate: Callable[[tuple[K, V]], bool]) -> Map[K, V]:  # type: ignore[override]
		return Map({k: v for k, v in self.items() if predicate((k, v))})

	# Kotlin: fun <K, V> Map<K, V>.filterKeys(predicate: (K) -> Boolean): Map<K, V>
	def filter_keys(self, predicate: Callable[[K], bool]) -> Map[K, V]:
		return Map({k: v for k, v in self.items() if predicate(k)})

	# Kotlin: fun <K, V> Map<K, V>.filterValues(predicate: (V) -> Boolean): Map<K, V>
	def filter_values(self, predicate: Callable[[V], bool]) -> Map[K, V]:
		return Map({k: v for k, v in self.items() if predicate(v)})

	# Kotlin: fun <K, V, R> Map<K, V>.map(transform: (Entry<K, V>) -> R): List<R>
	@override
	def map_(self, transformation: Callable[[tuple[K, V]], R]) -> List[R]:  # type: ignore
		from .list import List

		return List([transformation((k, v)) for k, v in self.items()])
