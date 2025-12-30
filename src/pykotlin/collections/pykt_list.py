import builtins
from typing import Iterable, TypeAlias, TypeVar
from typing import List as _List

from pykotlin.utils import inject_func_into

from .pykt_collections import (
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

T = TypeVar("T")


# DEFINITION
class kt_list(builtins.list):
    """
    A Kotlin-style list that extends Python's built-in list with additional functional methods.

    This class provides Kotlin-like operations such as filter_(), map_(), flatten(), distinct() and more, while maintaining full compatibility with Python's standard list type.
    """

    pass



List: TypeAlias = kt_list
"""Type alias for kt_list, providing Kotlin-style naming convention."""


# BELONGS ONLY TO LIST OBJECT
# Kotlin: fun <T> Iterable<Iterable<T>>.flatten(): List<T>
def flatten(self: Iterable[Iterable[T]]) -> _List[T]:
    """Returns a single list of all elements from all collections in the given collection."""
    flat_list: _List[T] = []

    for item in self:
        if isinstance(item, Iterable):
            flat_list.extend(item)
        else:
            raise ValueError("Item is not iterable.")

    return flat_list


# INJECTIONS
inject_func_into([builtins.list, kt_list], flatten)
inject_func_into([builtins.list, kt_list], filter_)
inject_func_into([builtins.list, kt_list], map_)
inject_func_into([builtins.list, kt_list], plus)
inject_func_into([builtins.list, kt_list], all_)
inject_func_into([builtins.list, kt_list], any_)
inject_func_into([builtins.list, kt_list], associate)
inject_func_into([builtins.list, kt_list], average)
inject_func_into([builtins.list, kt_list], contains)
inject_func_into([builtins.list, kt_list], contains_all)
inject_func_into([builtins.list, kt_list], distinct)
inject_func_into([builtins.list, kt_list], drop)
inject_func_into([builtins.list, kt_list], drop_last)
inject_func_into([builtins.list, kt_list], element_at)
inject_func_into([builtins.list, kt_list], element_at_or_null)
inject_func_into([builtins.list, kt_list], element_at_or_else)
inject_func_into([builtins.list, kt_list], find)
inject_func_into([builtins.list, kt_list], first)
inject_func_into([builtins.list, kt_list], first_not_null)
inject_func_into([builtins.list, kt_list], first_or_null)
inject_func_into([builtins.list, kt_list], count_)


# BELONG TO LIST IMPORT
def list_of(items: Iterable[T]) -> kt_list:
    return kt_list(items)


def empty_list() -> kt_list:
    return kt_list()
