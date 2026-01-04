from __future__ import annotations

import builtins

from typing import TYPE_CHECKING, Any

from kothonic.core_features import KotlinValue


if TYPE_CHECKING:
	from kothonic.collections import List

	from .int import Int
	from .float import Float


class String(str, KotlinValue[str]):
	"""
	A Kotlin-style string that extends Python's built-in str with additional functional methods.

	This class provides Kotlin-like operations such as to_int(), to_float(), trim(), substring(), and more, while maintaining full compatibility with Python's standard str type.
	"""

	@property
	def _kotlin_value(self) -> String:
		return self

	# Kotlin: fun String.toInt(): Int
	def to_int(self) -> Int:
		"""Parses the string as an Int number and returns the result."""
		from .int import Int

		return Int(int(self))

	# Kotlin: fun String.toIntOrNull(): Int?
	def to_int_or_null(self) -> Int | None:
		"""Parses the string as an Int number and returns the result or null if the string is not a valid representation of a number."""
		from .int import Int

		try:
			return Int(int(self))
		except Exception:
			return None

	# Kotlin: fun String.toFloat(): Float
	def to_float(self) -> Float:
		"""Parses the string as a Float number and returns the result."""
		from .float import Float

		return Float(float(self))

	# Kotlin: fun String.toFloatOrNull(): Float?
	def to_float_or_null(self) -> Float | None:
		"""Parses the string as a Float number and returns the result or null if the string is not a valid representation of a number."""
		from .float import Float

		try:
			return Float(float(self))
		except ValueError:
			return None

	# Kotlin: fun String?.isNullOrEmpty(): Boolean
	def is_null_or_empty(self) -> bool:
		"""Returns true if this char sequence is null or empty."""
		return self is None or self == ""

	# Kotlin: fun String?.isNullOrBlank(): Boolean
	def is_null_or_blank(self) -> bool:
		"""Returns true if this char sequence is null or empty or consists solely of whitespace characters."""
		return self is None or self.strip().replace(" ", "") == ""

	# Kotlin: fun String.reversed(): String
	def reversed_(self) -> String:
		"""Returns a sequence with characters in reversed order."""
		return String("".join(builtins.reversed(self)))

	# Kotlin: fun String.uppercase(): String
	def uppercase(self) -> String:
		"""Returns a copy of this string converted to upper case using the rules of the default locale."""
		return String(self.upper())

	# Kotlin: fun String.lowercase(): String
	def lowercase(self) -> String:
		"""Returns a copy of this string converted to lower case using the rules of the default locale."""
		return String(self.lower())

	# Kotlin: fun String.trim(): String
	def trim(self) -> String:
		"""Returns a string having leading and trailing whitespace removed."""
		return String(self.strip())

	# Kotlin: fun String.trimStart(): String
	def trim_start(self) -> String:
		"""Returns a string having leading whitespace removed."""
		return String(self.lstrip())

	# Kotlin: fun String.trimEnd(): String
	def trim_end(self) -> String:
		"""Returns a string having trailing whitespace removed."""
		return String(self.rstrip())

	# Kotlin: fun String.substring(startIndex: Int, endIndex: Int): String
	def substring(self, start: int, end: int) -> String:
		"""Returns a substring of this string that starts at the specified startIndex and continues to the index before endIndex."""
		return String(self[start:end])

	# Kotlin: operator fun String.contains(other: String): Boolean
	def contains(self, match: str) -> bool:
		"""Returns true if this string contains the other as a substring."""
		return match in self

	# Kotlin: fun String.startsWith(prefix: String, ignoreCase: Boolean = false): Boolean
	def starts_with(self, prefix: str, ignore_case: bool = False) -> bool:
		"""Returns true if this string starts with the specified prefix."""
		prefix = prefix.lower() if ignore_case else prefix
		compare_to = self.lower() if ignore_case else self
		return compare_to.startswith(prefix)

	# Kotlin: fun String.endsWith(suffix: String, ignoreCase: Boolean = false): Boolean
	def ends_with(self, suffix: str, ignore_case: bool = False) -> bool:
		"""Returns true if this string ends with the specified suffix."""
		suffix_check = suffix.lower() if ignore_case else suffix
		compare_to = self.lower() if ignore_case else self
		return compare_to.endswith(suffix_check)

	# Kotlin: operator fun String.plus(other: Any?): String
	def plus(self, other: Any) -> String:
		return String(self + str(other))

	# Kotlin: fun String.capitalize(): String
	def capitalize_(self) -> String:
		"""Returns a copy of this string having its first letter titlecased, or the original string if it's empty or already starts with a title case letter."""
		words = self.strip().split(" ")
		if not words:
			return String(self)
		first_word, remaining_words = (words[0], words[1:])
		return String(first_word.title() + " " + " ".join(remaining_words) if remaining_words else first_word.title())

	# Kotlin: fun String.take(n: Int): String
	def take(self, n: int) -> String:
		"""Returns a string containing the first n characters."""
		return String(self[:n])

	# Kotlin: fun String.takeLast(n: Int): String
	def take_last(self, n: int) -> String:
		"""Returns a string containing the last n characters."""
		length = len(self)
		return String(self[(length - n) :])

	# Kotlin: fun String.drop(n: Int): String
	def drop(self, n: int) -> String:
		"""Returns a string with the first n characters removed."""
		return String(self[n:])

	# Kotlin: fun String.dropLast(n: Int): String
	def drop_last(self, n: int) -> String:
		"""Returns a string with the last n characters removed."""
		length = len(self)
		return String(self[: (length - n)])

	# Kotlin: fun String.indexOf(string: String, startIndex: Int = 0, ignoreCase: Boolean = false): Int
	def index_of(self, string: str, start_index: int = 0, ignore_case: bool = False) -> Int:
		"""Returns the index within this string of the first occurrence of the specified string."""
		from .int import Int

		if ignore_case:
			return Int(self.lower().find(string.lower(), start_index))
		return Int(self.find(string, start_index))

	# Kotlin: fun Char.isDigit(): Boolean
	def is_digit(self) -> bool:
		"""Returns true if this string consists only of digits."""
		return self.isdigit()

	# Kotlin: fun String.toList(): List<Char>
	def to_list(self) -> List:
		"""Returns a List containing all characters."""
		from kothonic.collections import List

		return List(list(self))
