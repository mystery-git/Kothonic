import builtins
from typing import TypeAlias, Union

class kt_float(builtins.float):
    def to_int(self) -> builtins.int:
        """Returns the value of this number as an Int, which may involve rounding or truncation."""
        ...

    def to_int_or_null(self) -> Union[builtins.int, None]:
        """Parses the number as an Int and returns the result or null if not valid."""
        ...

    def to_string(self) -> builtins.str:
        """Returns a string representation of the object."""
        ...

Float: TypeAlias = kt_float
