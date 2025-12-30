import builtins
from typing import TypeAlias

from pykotlin.utils import inject_func_into


# DEFINITION
class kt_int(builtins.int):
    """
    A Kotlin-style integer that extends Python's built-in int with additional functional methods.

    This class provides Kotlin-like operations such as to_float(), to_string(), and more, while maintaining full compatibility with Python's standard int type.
    """

    pass


Int: TypeAlias = kt_int
"""Type alias for kt_int, providing Kotlin-style naming convention."""

# BELONGS ONLY TO INT OBJECT
# Kotlin: fun Number.toFloat(): Float
def to_float(self: builtins.int):
    """Returns the value of this number as a Float."""
    return float(self)


# Kotlin: Custom (no direct Int.toFloatOrNull)
def to_float_or_null(self: builtins.int):
    """Parses the number as a Float and returns the result or null if not valid."""
    try:
        return float(self)
    except ValueError:
        return None


# Kotlin: fun Any.toString(): String
def to_string(self: builtins.int):
    """Returns a string representation of the object."""
    return self.__str__()


# INJECTIONS
inject_func_into([builtins.int, kt_int], to_float)
inject_func_into([builtins.int, kt_int], to_float_or_null)
inject_func_into([builtins.int, kt_int], to_string)
