from __future__ import annotations

from typing import TYPE_CHECKING

from kothonic.core_features.kotlin_value import KotlinValue


if TYPE_CHECKING:
	from .byte import Byte
	from .long import Long
	from .float import Float
	from .short import Short
	from .double import Double


class Int(int, KotlinValue[int]):
	"""Integer that extends Python's built-in int with additional methods."""

	@property
	def _kotlin_value(self) -> Int:
		return self

	# Kotlin: fun Number.toByte(): Byte
	def to_byte(self) -> Byte:
		"""Returns the value of this number as a Byte, which may involve rounding or truncation."""
		from .byte import Byte

		return Byte(int(self))

	# Kotlin: fun Number.toDouble(): Double
	def to_double(self) -> Double:
		"""Returns the value of this number as a Double."""
		from .double import Double

		return Double(float(self))

	# Kotlin: fun Number.toFloat(): Float
	def to_float(self) -> Float:
		"""Returns the value of this number as a Float."""
		from .float import Float

		return Float(float(self))

	# Kotlin: fun Number.toInt(): Int
	def to_int(self) -> Int:
		"""Returns the value of this number as an Int."""
		return self

	# Kotlin: fun Number.toLong(): Long
	def to_long(self) -> Long:
		"""Returns the value of this number as a Long."""
		from .long import Long

		return Long(int(self))

	# Kotlin: fun Number.toShort(): Short
	def to_short(self) -> Short:
		"""Returns the value of this number as a Short, which may involve rounding or truncation."""
		from .short import Short

		return Short(int(self))

	# Kotlin: fun Int.toFloatOrNull(): Float? (Custom extension for consistency)
	def to_float_or_null(self) -> Float | None:
		from .float import Float

		try:
			return Float(float(self))
		except (ValueError, OverflowError):
			return None
