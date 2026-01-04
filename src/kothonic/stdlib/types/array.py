from typing import Generic, TypeVar

from kothonic.collections import List
from kothonic.core_features import KotlinValue


T = TypeVar("T")


class Array(Generic[T], list[T], KotlinValue[list[T]]):
	pass

	# TODO("")


def array_of(items: list | List) -> Array:
	return Array(items)


def empty_array() -> Array:
	return Array([])
