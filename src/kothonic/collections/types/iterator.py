from typing import TYPE_CHECKING, TypeVar, TypeAlias
from collections.abc import Generator


T = TypeVar("T")


if TYPE_CHECKING:
	Iterator: TypeAlias = Generator[T, None, None]
else:
	Iterator = Generator
