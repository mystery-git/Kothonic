from .dataclass_meta import Dataclass
from typing import cast
from dataclasses import replace
from typing import Any, Self


class Kt_Data(metaclass=Dataclass):
    """A class that inherits from this class will be considered a Dataclass.\n
    Configured to act like a Kotlin `data class` with a `copy()` method."""

    def copy(self, **changes: Any) -> Self:
        """Used to create a copy of the data class with the given changes (similar to Kotlin's data class `copy()` method.)"""
        return replace(cast(Any, self), **changes)
