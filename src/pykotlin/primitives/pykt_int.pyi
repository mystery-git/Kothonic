import builtins
from typing import TypeAlias, Union

class kt_int(builtins.int):
    def to_float(self) -> builtins.float:
        """Returns the value of this number as a Float."""
        ...

    def to_float_or_null(self) -> Union[builtins.float, None]:
        """Parses the number as a Float and returns the result or null if not valid."""
        ...

    def to_string(self) -> builtins.str:
        """Returns a string representation of the object."""
        ...

Int: TypeAlias = kt_int
