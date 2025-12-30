import builtins
from typing import TypeAlias, Union

from pykotlin.utils import inject_func_into


# DEFINITION
class kt_float(builtins.float):
    """
    A Kotlin-style float that extends Python's built-in float with additional functional methods.

    This class provides Kotlin-like operations such as to_int(), to_string(), and more, while maintaining full compatibility with Python's standard float type.
    """

    pass


Float: TypeAlias = kt_float
"""Type alias for kt_float, providing Kotlin-style naming convention."""


# BELONGS ONLY TO FLOAT OBJECT
# Kotlin: fun Number.toInt(): Int
def to_int(self: builtins.float) -> builtins.int:
    """Returns the value of this number as an Int, which may involve rounding or truncation."""
    return builtins.int(self)


# Kotlin: Custom
def to_int_or_null(self: builtins.float) -> Union[builtins.int, None]:
    """Parses the number as an Int and returns the result or null if not valid."""
    try:
        return builtins.int(self)
    except ValueError:
        return None


# Kotlin: fun Any.toString(): String
def to_string(self: builtins.float) -> builtins.str:
    """Returns a string representation of the object."""
    return self.__str__()


# INJECTIONS
inject_func_into([builtins.float, kt_float], to_int)
inject_func_into([builtins.float, kt_float], to_int_or_null)
inject_func_into([builtins.float, kt_float], to_string)
