from typing import TypeVar

from ..types.map import Map


K = TypeVar("K")
V = TypeVar("V")


# Kotlin: fun <K, V> mapOf(vararg pairs: Pair<K, V>): Map<K, V>
def map_of(items: dict[K, V] = {}) -> Map[K, V]:
	return Map(items)
