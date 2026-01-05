from __future__ import annotations

from typing import TYPE_CHECKING

from kothonic.core_features import KotlinValue


if TYPE_CHECKING:
	from .int import Int
	from .byte import Byte
	from .long import Long
	from .short import Short
	from .double import Double


class Float(float, KotlinValue[float]):
	"""
	A Kotlin-style float that extends Python's built-in float with additional functional methods.

	This class provides Kotlin-like operations such as to_int(), to_string(), and more, while maintaining full compatibility with Python's standard float type.
	"""

	@property
	def _kotlin_value(self) -> Float:
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
		return self

	# Kotlin: fun Number.toInt(): Int
	def to_int(self) -> Int:
		"""Returns the value of this number as an Int, which may involve rounding or truncation."""
		from .int import Int

		return Int(int(self))

	# Kotlin: fun Number.toLong(): Long
	def to_long(self) -> Long:
		"""Returns the value of this number as a Long, which may involve rounding or truncation."""
		from .long import Long

		return Long(int(self))

	# Kotlin: fun Number.toShort(): Short
	def to_short(self) -> Short:
		"""Returns the value of this number as a Short, which may involve rounding or truncation."""
		from .short import Short

		return Short(int(self))

	# Kotlin: fun Double.toIntOrNull(): Int? (Custom extension for consistency)
	def to_int_or_null(self) -> Int | None:
		"""
		Returns the value of this number as an Int, or null if the conversion fails.
		"""
		from .int import Int

		try:
			return Int(int(self))
		except (ValueError, OverflowError):
			return None
