
from typing import Any, Dict, Tuple, Type, MutableMapping

class SealedMeta(type):
    def __prepare__(metacls, name: str, bases: Tuple[type, ...], **kwargs: Any) -> MutableMapping[str, Any]: ...
    def __new__(mcs, name: str, bases: Tuple[type, ...], namespace: Dict[str, Any], **kwargs: Any) -> type: ...

class Kt_Sealed(metaclass=SealedMeta):
    def __class_getitem__(cls, item: Any) -> Any: ...

