from enum import EnumMeta

from .enum_sentinel import _EnumSentinel


class KotlinEnumMeta(EnumMeta):
	def __new__(mcs, name, bases, namespace, **kwargs):
		annotations = namespace.get("__annotations__", {})
		for member_name in annotations:
			if member_name not in namespace:
				namespace[member_name] = _EnumSentinel()
		return super().__new__(mcs, name, bases, namespace, **kwargs)
