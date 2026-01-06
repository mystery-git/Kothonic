from __future__ import annotations

import builtins
from typing import TYPE_CHECKING, Any

from kothonic.core_features import KotlinValue

if TYPE_CHECKING:
	from kothonic.stdlib.types.boolean import Boolean
	from kothonic.stdlib.types.byte import Byte
	from kothonic.stdlib.types.double import Double
	from kothonic.stdlib.types.float import Float
	from kothonic.stdlib.types.int import Int
	from kothonic.stdlib.types.long import Long
	from kothonic.stdlib.types.short import Short
	from kothonic.stdlib.types.string import String


class Char(builtins.str, KotlinValue[builtins.str]):
	def __new__(cls, value: str | int | Char):
		if isinstance(value, int):
			if not (0 <= value <= 0x10FFFF):
				raise ValueError(f"Char code point out of range: {value}")
			return super().__new__(cls, chr(value))
		elif isinstance(value, Char):
			return super().__new__(cls, str(value))
		else:
			if len(value) != 1:
				raise ValueError(f"Char has a length of one, not {len(value)}")
			return super().__new__(cls, value)

	@property
	def code(self) -> int:
		return ord(self)

	@property
	def _kotlin_value(self) -> builtins.str:
		return str(self)

	def compare_to(self, other: Char) -> Int:
		"""Compares this value with the specified value for order."""
		from kothonic.stdlib.types.int import Int

		return Int(ord(self) - ord(other))

	def plus(self, other: int) -> Char:
		"""Returns the char that is the result of adding the number to this char's code."""
		return Char(ord(self) + other)

	def minus(self, other: Char | int) -> Int | Char:
		"""
		If other is Char: Returns the difference between this char's code and the other char's code.
		If other is Int: Returns the char that is the result of subtracting the number from this char's code.
		"""
		from kothonic.stdlib.types.int import Int

		if isinstance(other, Char):
			return Int(ord(self) - ord(other))
		elif isinstance(other, int):
			return Char(ord(self) - other)
		else:
			raise TypeError(f"Unsupported operand type for minus: {type(other)}")

	def inc(self) -> Char:
		"""Returns the char that is the result of adding 1 to this char."""
		return Char(ord(self) + 1)

	def dec(self) -> Char:
		"""Returns the char that is the result of subtracting 1 from this char."""
		return Char(ord(self) - 1)

	def to_byte(self) -> Byte:
		"""Returns the value of this char as a Byte."""
		from kothonic.stdlib.types.byte import Byte
		return Byte(ord(self))

	def to_short(self) -> Short:
		"""Returns the value of this char as a Short."""
		from kothonic.stdlib.types.short import Short
		return Short(ord(self))

	def to_int(self) -> Int:
		"""Returns the value of this char as an Int."""
		from kothonic.stdlib.types.int import Int
		return Int(ord(self))

	def to_long(self) -> Long:
		"""Returns the value of this char as a Long."""
		from kothonic.stdlib.types.long import Long
		return Long(ord(self))

	def to_float(self) -> Float:
		"""Returns the value of this char as a Float."""
		from kothonic.stdlib.types.float import Float
		return Float(float(ord(self)))

	def to_double(self) -> Double:
		"""Returns the value of this char as a Double."""
		from kothonic.stdlib.types.double import Double
		return Double(float(ord(self)))

	def equals(self, other: Any) -> Boolean:
		"""Indicates whether some other object is "equal to" this one."""
		from kothonic.stdlib.types.boolean import Boolean
		if isinstance(other, Char):
			return Boolean(str(self) == str(other))
		return Boolean(False)

	def hash_code(self) -> Int:
		"""Returns a hash code value for the object."""
		from kothonic.stdlib.types.int import Int
		return Int(hash(self))

	def to_string(self) -> String:
		"""Returns a String object representing this Char."""
		from kothonic.stdlib.types.string import String
		return String(self)

	# Character properties
	def is_digit(self) -> Boolean:
		"""Returns true if this character is a digit."""
		from kothonic.stdlib.types.boolean import Boolean
		return Boolean(self.isdigit())

	def is_letter(self) -> Boolean:
		"""Returns true if this character is a letter."""
		from kothonic.stdlib.types.boolean import Boolean
		return Boolean(self.isalpha())

	def is_letter_or_digit(self) -> Boolean:
		"""Returns true if this character is a letter or digit."""
		from kothonic.stdlib.types.boolean import Boolean
		return Boolean(self.isalnum())

	def is_lower_case(self) -> Boolean:
		"""Returns true if this character is lower case."""
		from kothonic.stdlib.types.boolean import Boolean
		return Boolean(self.islower())

	def is_upper_case(self) -> Boolean:
		"""Returns true if this character is upper case."""
		from kothonic.stdlib.types.boolean import Boolean
		return Boolean(self.isupper())

	def is_whitespace(self) -> Boolean:
		"""Returns true if this character is whitespace."""
		from kothonic.stdlib.types.boolean import Boolean
		return Boolean(self.isspace())

	def to_lower_case(self) -> Char:
		"""Converts this character to lower case."""
		return Char(self.lower())

	def to_upper_case(self) -> Char:
		"""Converts this character to upper case."""
		return Char(self.upper())
