import builtins
from typing import Iterable, TypeAlias, TypeVar

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

T = TypeVar("T")


# DEFINITION
class kt_set(builtins.set):
    """
    A Kotlin-style set that extends Python's built-in set with additional functional methods.

    This class provides Kotlin-like operations such as filter_(), map_(), distinct(), and more, while maintaining full compatibility with Python's standard set type.
    """

    pass


Set: TypeAlias = kt_set
"""Type alias for kt_set, providing Kotlin-style naming convention."""

# INJECTIONS
inject_func_into([builtins.set, kt_set], filter_)
inject_func_into([builtins.set, kt_set], map_)
inject_func_into([builtins.set, kt_set], plus)
inject_func_into([builtins.set, kt_set], all_)
inject_func_into([builtins.set, kt_set], any_)
inject_func_into([builtins.set, kt_set], associate)
inject_func_into([builtins.set, kt_set], average)
inject_func_into([builtins.set, kt_set], contains)
inject_func_into([builtins.set, kt_set], contains_all)
inject_func_into([builtins.set, kt_set], count_)
inject_func_into([builtins.set, kt_set], distinct)
inject_func_into([builtins.set, kt_set], drop)
inject_func_into([builtins.set, kt_set], drop_last)
inject_func_into([builtins.set, kt_set], element_at)
inject_func_into([builtins.set, kt_set], element_at_or_null)
inject_func_into([builtins.set, kt_set], element_at_or_else)
inject_func_into([builtins.set, kt_set], find)
inject_func_into([builtins.set, kt_set], first)
inject_func_into([builtins.set, kt_set], first_not_null)
inject_func_into([builtins.set, kt_set], first_or_null)


# BELONG TO SET IMPORT
def set_of(items: Iterable[T]) -> kt_set:
    return kt_set(items)


def empty_set() -> kt_set:
    return kt_set()
