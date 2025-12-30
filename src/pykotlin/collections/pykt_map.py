import builtins
from typing import Dict, TypeAlias, TypeVar

from pykotlin.collections.pykt_collections import (
    all_,
    any_,
    associate,
    average,
    contains,
    contains_all,
    count_,
    distinct,
    drop,
    drop_last,
    element_at,
    element_at_or_else,
    element_at_or_null,
    filter_,
    find,
    first,
    first_not_null,
    first_or_null,
    map_,
    plus,
)
from pykotlin.utils import inject_func_into

K = TypeVar("K")
V = TypeVar("V")


# DEFINITION
class kt_map(builtins.dict):
    """
    A Kotlin-style map that extends Python's built-in dict with additional functional methods.

    This class provides Kotlin-like operations such as contains_key(), contains_value(), filter_(), map_(), plus(), all_(), any_(), associate(), average(), and more, while maintaining full compatibility with Python's standard dict type.
    """

    pass



Map: TypeAlias = kt_map
"""Type alias for kt_map, providing Kotlin-style naming convention."""


# BELONGS ONLY TO MAP OBJECT
# Kotlin: fun <K, V> Map<K, V>.containsKey(key: K): Boolean
def contains_key(self: Dict[K, V], key: K) -> bool:
    """Returns true if the map contains the specified key."""
    return key in self.keys()


# Kotlin: fun <K, V> Map<K, V>.containsValue(value: V): Boolean
def contains_value(self: Dict[K, V], value: V) -> bool:
    """Returns true if the map maps one or more keys to the specified value."""
    return value in self.values()


# INJECTIONS
inject_func_into([builtins.dict, kt_map], contains_key)
inject_func_into([builtins.dict, kt_map], contains_value)

inject_func_into([builtins.dict, kt_map], filter_)
inject_func_into([builtins.dict, kt_map], map_)
inject_func_into([builtins.dict, kt_map], plus)
inject_func_into([builtins.dict, kt_map], all_)
inject_func_into([builtins.dict, kt_map], any_)
inject_func_into([builtins.dict, kt_map], associate)
inject_func_into([builtins.dict, kt_map], average)
inject_func_into([builtins.dict, kt_map], contains)
inject_func_into([builtins.dict, kt_map], contains_all)
inject_func_into([builtins.dict, kt_map], count_)
inject_func_into([builtins.dict, kt_map], distinct)
inject_func_into([builtins.dict, kt_map], drop)
inject_func_into([builtins.dict, kt_map], drop_last)
inject_func_into([builtins.dict, kt_map], element_at)
inject_func_into([builtins.dict, kt_map], element_at_or_null)
inject_func_into([builtins.dict, kt_map], element_at_or_else)
inject_func_into([builtins.dict, kt_map], find)
inject_func_into([builtins.dict, kt_map], first)
inject_func_into([builtins.dict, kt_map], first_not_null)
inject_func_into([builtins.dict, kt_map], first_or_null)


# BELONG TO MAP IMPORT
def map_of(items: Dict[K, V]) -> kt_map:
    return kt_map(items)


def empty_map() -> kt_map:
    return kt_map()
