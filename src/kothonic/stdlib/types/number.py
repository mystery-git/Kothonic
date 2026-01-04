from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable


if TYPE_CHECKING:
	from .int import Int
	from .byte import Byte
	from .long import Long
	from .float import Float
	from .short import Short
	from .double import Double


@runtime_checkable
class Number(Protocol):
	def to_byte(self) -> Byte: ...
	def to_double(self) -> Double: ...
	def to_float(self) -> Float: ...
	def to_int(self) -> Int: ...
	def to_long(self) -> Long: ...
	def to_short(self) -> Short: ...
