from typing import TYPE_CHECKING, Any

from .sealed_meta import SealedMeta


class Sealed(metaclass=SealedMeta):
	"""
	A base class for Kotlin-like sealed classes.

	To satisfy static analysis tools (mypy, ty, etc.) and avoid "class is not defined"
	errors, nested classes should inherit from Kt_Sealed instead of the parent class name.
	The metaclass will automatically reparent them at runtime.

	Example (Statically safe):
		class Expr(Sealed):
			class Const(Sealed):
				value: int
			class Sum(Sealed):
				left: 'Expr'
				right: 'Expr'

	Example (Legacy/Runtime hack):
		class Expr(Sealed):
			class Const(Expr):
				value: int
	"""

	if TYPE_CHECKING:

		def __class_getitem__(cls, item: Any) -> Any: ...
