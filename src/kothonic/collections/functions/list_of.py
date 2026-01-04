from typing import TypeVar
from collections.abc import Iterable

from ..types.list import List


T = TypeVar("T")


# Kotlin: fun <T> listOf(vararg elements: T): List<T>
def list_of(items: Iterable[T] = []) -> List[T]:
	return List(items)
