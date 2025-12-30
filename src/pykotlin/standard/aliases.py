import builtins
from abc import ABC
from collections.abc import Callable
from typing import Any as Anything
from typing import NoReturn, Optional, TypeAlias, Union, TypeVar, ParamSpec, TYPE_CHECKING

T = TypeVar("T")
P = ParamSpec("P")
R = TypeVar("R")

# Hierarchy
Any: TypeAlias = Anything
Nothing: TypeAlias = NoReturn
Number: TypeAlias = Union[builtins.int, builtins.float]

# Nullability / Void
Unit = None
null = None

if TYPE_CHECKING:
    Nullable: TypeAlias = Optional[T]
else:
    Nullable = Optional

# Exception Handling
Throwable: TypeAlias = builtins.Exception

# OOP
Interface: TypeAlias = ABC

# Collections
Collection: TypeAlias = Union[builtins.list, builtins.dict, builtins.set]

# Functional
if TYPE_CHECKING:
    fun = Callable[P, R]
else:
    fun = Callable
