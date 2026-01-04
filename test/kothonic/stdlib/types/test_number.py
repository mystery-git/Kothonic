from kothonic.stdlib.types.int import Int
from kothonic.stdlib.types.byte import Byte
from kothonic.stdlib.types.long import Long
from kothonic.stdlib.types.float import Float
from kothonic.stdlib.types.short import Short
from kothonic.stdlib.types.double import Double
from kothonic.stdlib.types.number import Number


def test_int_conversions():
	i = Int(10)
	assert isinstance(i, Number)
	assert i.to_byte() == 10
	assert isinstance(i.to_byte(), Byte)
	assert i.to_double() == 10.0
	assert isinstance(i.to_double(), Double)
	assert i.to_float() == 10.0
	assert isinstance(i.to_float(), Float)
	assert i.to_int() is i
	assert i.to_long() == 10
	assert isinstance(i.to_long(), Long)
	assert i.to_short() == 10
	assert isinstance(i.to_short(), Short)


def test_double_conversions():
	d = Double(10.5)
	assert isinstance(d, Number)
	assert d.to_byte() == 10
	assert isinstance(d.to_byte(), Byte)
	assert d.to_double() is d
	assert d.to_float() == 10.5
	assert isinstance(d.to_float(), Float)
	assert d.to_int() == 10
	assert isinstance(d.to_int(), Int)
	assert d.to_long() == 10
	assert isinstance(d.to_long(), Long)
	assert d.to_short() == 10
	assert isinstance(d.to_short(), Short)


def test_float_conversions():
	f = Float(10.5)
	assert isinstance(f, Number)
	assert f.to_byte() == 10
	assert isinstance(f.to_byte(), Byte)
	assert f.to_double() == 10.5
	assert isinstance(f.to_double(), Double)
	assert f.to_float() is f
	assert f.to_int() == 10
	assert isinstance(f.to_int(), Int)
	assert f.to_long() == 10
	assert isinstance(f.to_long(), Long)
	assert f.to_short() == 10
	assert isinstance(f.to_short(), Short)


def test_number_inheritance():
	assert issubclass(Int, Number)
	assert issubclass(Double, Number)
	assert issubclass(Float, Number)
	assert issubclass(Long, Number)
	assert issubclass(Short, Number)
	assert issubclass(Byte, Number)
