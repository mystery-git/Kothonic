import builtins
from typing import TypeAlias, Union

class kt_str(builtins.str):
    def to_int(self) -> builtins.int:
        """Parses the string as an Int number and returns the result."""
        ...

    def to_int_or_null(self) -> Union[builtins.int, None]:
        """Parses the string as an Int number and returns the result or null if the string is not a valid representation of a number."""
        ...

    def to_float(self) -> builtins.float:
        """Parses the string as a Float number and returns the result."""
        ...

    def to_float_or_null(self) -> Union[builtins.float, None]:
        """Parses the string as a Float number and returns the result or null if the string is not a valid representation of a number."""
        ...

    def is_null_or_empty(self) -> builtins.bool:
        """Returns true if this char sequence is null or empty."""
        ...

    def is_null_or_blank(self) -> builtins.bool:
        """Returns true if this char sequence is null or empty or consists solely of whitespace characters."""
        ...

    def reverse(self) -> builtins.str:
        """Returns a sequence with characters in reversed order."""
        ...

    def uppercase(self) -> builtins.str:
        """Returns a copy of this string converted to upper case using the rules of the default locale."""
        ...

    def lowercase(self) -> builtins.str:
        """Returns a copy of this string converted to lower case using the rules of the default locale."""
        ...

    def trim(self) -> builtins.str:
        """Returns a string having leading and trailing whitespace removed."""
        ...

    def trim_start(self) -> builtins.str:
        """Returns a string having leading whitespace removed."""
        ...

    def trim_end(self) -> builtins.str:
        """Returns a string having trailing whitespace removed."""
        ...

    def substring(self, start: builtins.int, end: builtins.int) -> builtins.str:
        """Returns a substring of this string that starts at the specified startIndex and continues to the index before endIndex."""
        ...

    def contains(self, match: builtins.str) -> builtins.bool:
        """Returns true if this char sequence contains the specified other char sequence as a substring."""
        ...

    def starts_with(
        self, match: Union[builtins.str, builtins.tuple[builtins.str]]
    ) -> builtins.bool:
        """Returns true if this string starts with the specified prefix."""
        ...

    def ends_with(
        self, match: Union[builtins.str, builtins.tuple[builtins.str]]
    ) -> builtins.bool:
        """Returns true if this string ends with the specified suffix."""
        ...

    def capitalize_(self) -> builtins.str:
        """Returns a copy of this string having its first letter titlecased, or the original string if it's empty or already starts with a title case letter."""
        ...

    def plus(self, other: builtins.str) -> builtins.str:
        """Returns a string obtained by concatenating this string with the string representation of the given other object."""
        ...

    def take(self, chars: builtins.int) -> builtins.str:
        """Returns a string containing the first n characters."""
        ...

    def take_last(self, chars: builtins.int) -> builtins.str:
        """Returns a string containing the last n characters."""
        ...

    def drop(self, chars: builtins.int) -> builtins.str:
        """Returns a string with the first n characters removed."""
        ...

    def drop_last(self, chars: builtins.int) -> builtins.str:
        """Returns a string with the last n characters removed."""
        ...

    def index_of(self, match: builtins.str) -> builtins.int:
        """Returns the index within this string of the first occurrence of the specified string."""
        ...

    def is_digit(self) -> bool:
        """Returns true if this string consists only of digits."""
        ...

    def to_list(self) -> builtins.list:
        """Returns a List containing all characters."""
        ...

String: TypeAlias = str
