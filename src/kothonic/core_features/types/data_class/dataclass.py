from typing import Any, cast
from dataclasses import replace

from typing_extensions import Self

from .dataclass_meta import MetaDataclass


class Data(metaclass=MetaDataclass):
	"""Provides Kotlin-like data class behaviour."""

	def copy(self, **changes: Any) -> Self:
		"""Creates a copy with the given changes."""

		return replace(cast(Any, self), **changes)
