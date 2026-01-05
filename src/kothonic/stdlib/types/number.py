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
	"""
	Abstract class representing a number.
	"""

	# Kotlin: abstract fun toByte(): Byte
	def to_byte(self) -> Byte:
		"""
		Returns the value of this number as a Byte, which may involve rounding or truncation.
		"""
		...

	# Kotlin: abstract fun toDouble(): Double
	def to_double(self) -> Double:
		"""
		Returns the value of this number as a Double.
		"""
		...

	# Kotlin: abstract fun toFloat(): Float
	def to_float(self) -> Float:
		"""
		Returns the value of this number as a Float.
		"""
		...

	# Kotlin: abstract fun toInt(): Int
	def to_int(self) -> Int:
		"""
		Returns the value of this number as an Int, which may involve rounding or truncation.
		"""
		...

	# Kotlin: abstract fun toLong(): Long
	def to_long(self) -> Long:
		"""
		Returns the value of this number as a Long, which may involve rounding or truncation.
		"""
		...

	# Kotlin: abstract fun toShort(): Short
	def to_short(self) -> Short:
		"""
		Returns the value of this number as a Short, which may involve rounding or truncation.
		"""
		...
