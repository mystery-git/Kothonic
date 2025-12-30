import builtins
from typing import List, TypeAlias, Union

from pykotlin.utils import inject_func_into


# DEFINITION
class kt_str(builtins.str):
    """
    A Kotlin-style string that extends Python's built-in str with additional functional methods.

    This class provides Kotlin-like operations such as to_int(), to_float(), trim(), substring(), and more, while maintaining full compatibility with Python's standard str type.
    """

    pass



String: TypeAlias = str
"""Type alias for the built-in str type, providing Kotlin-style naming convention."""

# BELONGS ONLY TO STRING OBJECT
# Kotlin: fun String.toInt(): Int
def to_int(self: builtins.str) -> builtins.int:
    """Parses the string as an Int number and returns the result."""
    return builtins.int(self)


# Kotlin: fun String.toIntOrNull(): Int?
def to_int_or_null(self: builtins.str) -> Union[builtins.int, None]:
    """Parses the string as an Int number and returns the result or null if the string is not a valid representation of a number."""
    try:
        return builtins.int(self)
    except ValueError:
        return None


# Kotlin: fun String.toFloat(): Float
def to_float(self: builtins.str) -> builtins.float:
    """Parses the string as a Float number and returns the result."""
    return builtins.float(self)


# Kotlin: fun String.toFloatOrNull(): Float?
def to_float_or_null(self: builtins.str) -> Union[builtins.float, None]:
    """Parses the string as a Float number and returns the result or null if the string is not a valid representation of a number."""
    try:
        return builtins.float(self)
    except ValueError:
        return None


# Kotlin: fun CharSequence?.isNullOrEmpty(): Boolean
def is_null_or_empty(self: Union[builtins.str, None]) -> builtins.bool:
    """Returns true if this char sequence is null or empty."""
    return self is None or self == ""


# Kotlin: fun CharSequence?.isNullOrBlank(): Boolean
def is_null_or_blank(self: Union[builtins.str, None]) -> builtins.bool:
    """Returns true if this char sequence is null or empty or consists solely of whitespace characters."""
    return self is None or self.strip().replace(" ", "") == ""


# Kotlin: fun CharSequence.reversed(): CharSequence
def reverse(self: builtins.str) -> builtins.str:
    """Returns a sequence with characters in reversed order."""
    return self[::-1]


# Kotlin: fun String.uppercase(): String
def uppercase(self: builtins.str) -> builtins.str:
    """Returns a copy of this string converted to upper case using the rules of the default locale."""
    return self.upper()


# Kotlin: fun String.lowercase(): String
def lowercase(self: builtins.str) -> builtins.str:
    """Returns a copy of this string converted to lower case using the rules of the default locale."""
    return self.lower()


# Kotlin: fun String.trim(): String
def trim(self: builtins.str) -> builtins.str:
    """Returns a string having leading and trailing whitespace removed."""
    return self.strip()


# Kotlin: fun String.trimStart(): String
def trim_start(self: builtins.str) -> builtins.str:
    """Returns a string having leading whitespace removed."""
    return self.lstrip()


# Kotlin: fun String.trimEnd(): String
def trim_end(self: builtins.str) -> builtins.str:
    """Returns a string having trailing whitespace removed."""
    return self.rstrip()


# Kotlin: fun String.substring(startIndex: Int, endIndex: Int): String
def substring(
    self: builtins.str, start: builtins.int, end: builtins.int
) -> builtins.str:
    """Returns a substring of this string that starts at the specified startIndex and continues to the index before endIndex."""
    return self[start:end]


# Kotlin: operator fun CharSequence.contains(other: CharSequence): Boolean
def contains(self: builtins.str, match: builtins.str) -> builtins.bool:
    """Returns true if this char sequence contains the specified other char sequence as a substring."""
    return self.__contains__(match)


# Kotlin: fun String.startsWith(prefix: String, ignoreCase: Boolean = false): Boolean
def starts_with(
    self: builtins.str, match: Union[builtins.str, tuple[builtins.str]]
) -> builtins.bool:
    """Returns true if this string starts with the specified prefix."""
    return self.startswith(match)


# Kotlin: fun String.endsWith(suffix: String, ignoreCase: Boolean = false): Boolean
def ends_with(
    self: builtins.str, match: Union[builtins.str, tuple[builtins.str]]
) -> builtins.bool:
    """Returns true if this string ends with the specified suffix."""
    return self.endswith(match)


# Kotlin: fun String.capitalize(): String
def capitalize_(self: builtins.str) -> builtins.str:
    """Returns a copy of this string having its first letter titlecased, or the original string if it's empty or already starts with a title case letter."""
    words: List[builtins.str] = self.strip().split(" ")

    first_word, remaining_words = (words[0], words[1:])

    return first_word.title() + " ".join(remaining_words)


# Kotlin: operator fun String.plus(other: Any?): String
def plus(self: builtins.str, other: builtins.str) -> builtins.str:
    """Returns a string obtained by concatenating this string with the string representation of the given other object."""
    return self + other


# Kotlin: fun String.take(n: Int): String
def take(self: builtins.str, chars: builtins.int) -> builtins.str:
    """Returns a string containing the first n characters."""
    return self[:chars]


# Kotlin: fun String.takeLast(n: Int): String
def take_last(self: builtins.str, chars: builtins.int) -> builtins.str:
    """Returns a string containing the last n characters."""
    length = len(self)
    return self[(length - chars) :]


# Kotlin: fun String.drop(n: Int): String
def drop(self: builtins.str, chars: builtins.int) -> builtins.str:
    """Returns a string with the first n characters removed."""
    return self[chars:]


# Kotlin: fun String.dropLast(n: Int): String
def drop_last(self: builtins.str, chars: builtins.int) -> builtins.str:
    """Returns a string with the last n characters removed."""
    length = len(self)
    return self[: (length - chars)]


# Kotlin: fun String.indexOf(string: String, startIndex: Int = 0, ignoreCase: Boolean = false): Int
def index_of(self: builtins.str, match: builtins.str) -> builtins.int:
    """Returns the index within this string of the first occurrence of the specified string."""
    return self.index(match)


# Kotlin: fun Char.isDigit(): Boolean (Note: applying to whole string here)
def is_digit(self: builtins.str) -> bool:
    """Returns true if this string consists only of digits."""
    return self.isdigit()


# Kotlin: fun CharSequence.toList(): List<Char>
def to_list(self: builtins.str) -> List:
    """Returns a List containing all characters."""
    return list(self)


# INJECTIONS
inject_func_into([builtins.str, kt_str], to_int_or_null)
inject_func_into([builtins.str, kt_str], to_int)
inject_func_into([builtins.str, kt_str], to_float)
inject_func_into([builtins.str, kt_str], to_float_or_null)
inject_func_into([builtins.str, kt_str], is_null_or_empty)
inject_func_into([builtins.str, kt_str], is_null_or_blank)
inject_func_into([builtins.str, kt_str], reverse)
inject_func_into([builtins.str, kt_str], uppercase)
inject_func_into([builtins.str, kt_str], lowercase)
inject_func_into([builtins.str, kt_str], trim)
inject_func_into([builtins.str, kt_str], trim_start)
inject_func_into([builtins.str, kt_str], trim_end)
inject_func_into([builtins.str, kt_str], substring)
inject_func_into([builtins.str, kt_str], contains)
inject_func_into([builtins.str, kt_str], starts_with)
inject_func_into([builtins.str, kt_str], ends_with)
inject_func_into([builtins.str, kt_str], capitalize_)
inject_func_into([builtins.str, kt_str], plus)
inject_func_into([builtins.str, kt_str], take)
inject_func_into([builtins.str, kt_str], take_last)
inject_func_into([builtins.str, kt_str], drop)
inject_func_into([builtins.str, kt_str], drop_last)
inject_func_into([builtins.str, kt_str], index_of)
inject_func_into([builtins.str, kt_str], is_digit)
inject_func_into([builtins.str, kt_str], to_list)
