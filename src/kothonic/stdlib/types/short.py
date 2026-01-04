from __future__ import annotations

from typing import TYPE_CHECKING

from kothonic.core_features import KotlinValue


if TYPE_CHECKING:
	from .int import Int
	from .byte import Byte
	from .long import Long
	from .float import Float
	from .double import Double


class Short(int, KotlinValue[int]):
	"""
	A Kotlin-style Short that extends Python's built-in int.
	"""

	@property
	def _kotlin_value(self) -> Short:
		return self

	# Kotlin: fun Number.toByte(): Byte
	def to_byte(self) -> Byte:
		from .byte import Byte

		return Byte(int(self))

	# Kotlin: fun Number.toDouble(): Double
	def to_double(self) -> Double:
		from .double import Double

		return Double(float(self))

	# Kotlin: fun Number.toFloat(): Float
	def to_float(self) -> Float:
		from .float import Float

		return Float(float(self))

	# Kotlin: fun Number.toInt(): Int
	def to_int(self) -> Int:
		from .int import Int

		return Int(self)

	# Kotlin: fun Number.toLong(): Long
	def to_long(self) -> Long:
		from .long import Long

		return Long(int(self))

	# Kotlin: fun Number.toShort(): Short
	def to_short(self) -> Short:
		return self
