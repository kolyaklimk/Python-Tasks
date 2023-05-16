import unittest
from MySerializer.Factory import Factory
from MySerializer.Factory import SerializerType

''' Constants'''
FOR_TEST = [1436, 74, 1, 6, 4315.64, "string", bytes([6, 17, 5]), "[1 , 2, 3, 5]", bytearray([3, 7, 9]), 153 + 3j,
            {15, 2, 523, 76, 4}, None, (21, 5424, 53, 212, 65), frozenset({1, 2}), [], [1, 2, 3],
            {41: {153: {151: {163: 64}}}}, 6243, 6, 7, 134, 6, "asdsafas", "cdsaf asdf 43fdsa", '432412', "fafae", 5312,
            6, 123, 2 + 6j, [53, 51, 56], ("dasd", "gdvc", "65324"), True, False]


class TestClass:
    @staticmethod
    def test_string():
        return "tst5"

    @classmethod
    def test_classmethod(cls):
        return cls._test_v

    def func(self):
        return 1

    _test_v = 14 / 2 - 7 * 2


class TestClass2(TestClass):
    A = 5
    B = 66
    C = 41
    _X = 53

    @staticmethod
    def tst4():
        return 421 + TestClass2._X

    def init(self):
        self.xy = 10

    def inf(self):
        print(self.xy, " ", self._test_v)


def rec_func(a):
    return rec_func(a - 1) + 1 if a > 1 else 1


def for_dec(a):
    return 7 * a


def my_dec(func):
    def wrapper(*args, **kwargs):
        return 50 * func(*args, **kwargs)

    return wrapper


def gen():
    for i in range(7):
        yield i + 2


decorated_func = my_dec(for_dec)
