from enum import EnumMeta
from .kt_enum_sentinel import _KtEnumSentinel

class _KtEnumMeta(EnumMeta):
    def __new__(mcs, name, bases, namespace, **kwargs):
        annotations = namespace.get('__annotations__', {})
        for member_name in annotations:
             if member_name not in namespace:
                 namespace[member_name] = _KtEnumSentinel()
        return super().__new__(mcs, name, bases, namespace, **kwargs)
