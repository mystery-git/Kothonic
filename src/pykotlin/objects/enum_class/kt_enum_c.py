from enum import Enum
import builtins
from typing import Any, List, Type, TypeVar
from .kt_enum_sentinel import _KtEnumSentinel
from .kt_enum_meta import _KtEnumMeta

T = TypeVar("T", bound="Kt_Enum")

class Kt_Enum(Enum, metaclass = _KtEnumMeta):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        first_type: Type[Any] | None = None
        
        for member in cls:
            val_type = type(member.value)
            if first_type is None:
                first_type = val_type
            elif val_type != first_type:
                 raise TypeError(f"Type mismatch in {cls.__name__}: {val_type} != {first_type}. All enum members must have the same type.")

    @property
    def value(self) -> Any:
        if isinstance(self._value_, _KtEnumSentinel):
            return None
        return self._value_

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        # 0-based ordinal behavior (Kotlin style)
        return count

    @property
    def ordinal(self) -> builtins.int:
        return list(self.__class__._member_names_).index(self.name)
    
    @classmethod
    def value_of(cls: Type[T], name: builtins.str) -> T:
        return cls[name]
    
    @classmethod
    def values(cls: Type[T]) -> List[T]:
        return list(cls)

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.ordinal < other.ordinal
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.ordinal > other.ordinal
        return NotImplemented
    
    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.ordinal <= other.ordinal
        return NotImplemented

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.ordinal >= other.ordinal
        return NotImplemented
