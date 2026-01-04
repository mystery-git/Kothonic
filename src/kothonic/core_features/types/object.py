import threading

from typing import final


class Singleton(type):
	_instances = {}
	_lock = threading.Lock()

	@final
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			with cls._lock:
				if cls not in cls._instances:
					cls._instances[cls] = super().__call__(*args, **kwargs)

		return cls._instances[cls]


class Object(metaclass=Singleton):
	"""Enables Kotlin-like 'object' behaviour."""

	pass
