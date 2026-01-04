from dataclasses import dataclass

import pytest  # ty: ignore[unresolved-import]

from kothonic.core_features import Sealed


def test_sealed_explicit_subclassing():
	class Base(Sealed):
		class A(Base):
			pass  # ty: ignore[unresolved-reference] # noqa: F821

		class B(Base):
			pass  # ty: ignore[unresolved-reference] # noqa: F821

		class C:
			pass  # Not a subclass

	assert issubclass(Base.A, Base)
	assert issubclass(Base.B, Base)
	assert not issubclass(Base.C, Base)
	assert isinstance(Base.A(), Base)
	assert isinstance(Base.B(), Base)
	assert not isinstance(Base.C(), Base)


def test_sealed_dataclass_explicit():
	class Base(Sealed):
		@dataclass
		class A(Base):  # ty: ignore[unresolved-reference] # noqa: F821
			x: int

		@dataclass
		class B(Base):  # ty: ignore[unresolved-reference] # noqa: F821
			y: str

	a = Base.A(10)
	b = Base.B("hello")

	assert isinstance(a, Base)
	assert a.x == 10
	assert isinstance(b, Base)
	assert b.y == "hello"


def test_sealed_methods_explicit():
	class Base(Sealed):
		def base_method(self):
			return "base"

		class A(Base):  # ty: ignore[unresolved-reference] # noqa: F821
			def a_method(self):
				return "a"

	inst = Base.A()
	assert inst.base_method() == "base"
	assert inst.a_method() == "a"


def test_isinstance_matching_explicit():
	class Expr(Sealed):
		@dataclass
		class Const(Expr):  # ty: ignore[unresolved-reference] # noqa: F821
			value: int

		@dataclass
		class Sum(Expr):  # ty: ignore[unresolved-reference] # # noqa: F821
			left: "Expr"
			right: "Expr"

	def eval(e: Expr) -> int:
		if isinstance(e, Expr.Const):
			return e.value
		if isinstance(e, Expr.Sum):
			return eval(e.left) + eval(e.right)  # ty: ignore[invalid-argument-type]
		return 0

	res = eval(Expr.Sum(Expr.Const(1), Expr.Const(2)))  # ty: ignore[invalid-argument-type]
	assert res == 3


def test_sealed_with_literals():
	class Result(Sealed):
		@dataclass
		class Success(Result):  # ty: ignore[unresolved-reference] # noqa: F821
			data: list

		@dataclass
		class Error(Result):  # ty: ignore[unresolved-reference] # noqa: F821
			details: dict

	s = Result.Success([1, 2, 3])
	e = Result.Error({"code": 404, "msg": "Not Found"})

	assert isinstance(s, Result)
	assert isinstance(e, Result)
	assert s.data == [1, 2, 3]
	assert e.details["code"] == 404


if __name__ == "__main__":
	pytest.main([__file__])
