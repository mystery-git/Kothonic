from dataclasses import dataclass
from typing import dataclass_transform


@dataclass_transform(frozen_default=True, field_specifiers=(dataclass,))
class Dataclass(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)

        # Stop here to avoid recursion or conflict.
        if "__slots__" in namespace:
            return cls

        return dataclass(frozen=True, slots=True, init = True)(cls)
