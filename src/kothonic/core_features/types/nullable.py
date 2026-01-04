from typing import TYPE_CHECKING, TypeVar, Optional, TypeAlias


T = TypeVar("T")

if TYPE_CHECKING:
	Nullable: TypeAlias = T | None
else:
	Nullable = Optional

if TYPE_CHECKING:
	N: TypeAlias = T | None
else:
	N = Nullable
