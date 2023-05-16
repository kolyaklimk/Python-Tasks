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


class SerializationTestCase(unittest.TestCase):
    json = Factory.create_serializer(SerializerType.JSON)
    xml = Factory.create_serializer(SerializerType.XML)

    def test_json(self):
        test = self.json.dumps(FOR_TEST)
        test = self.json.loads(test)

        self.assertEqual(FOR_TEST, test)

    def test_xml(self):
        test = self.xml.dumps(FOR_TEST)
        test = self.xml.loads(test)

        self.assertEqual(FOR_TEST, test)

    def test_json_class(self):
        test_cl = self.json.dumps(TestClass2)
        test_cl = self.json.loads(test_cl)

        orig = [TestClass2.A, TestClass2.B, TestClass2.C, TestClass2._X, TestClass2.tst4(), TestClass2.test_string(),
                TestClass2.test_classmethod(), ]
        my_ser = [test_cl.A, test_cl.B, test_cl.C, test_cl._X, test_cl.tst4(), test_cl.test_string(),
                  test_cl.test_classmethod()]

        self.assertEqual(orig, my_ser)

    def test_xml_class(self):
        test_cl = self.xml.dumps(TestClass2)
        test_cl = self.xml.loads(test_cl)

        orig = [TestClass2.A, TestClass2.B, TestClass2.C, TestClass2._X, TestClass2.tst4(), TestClass2.test_string()]
        my_ser = [test_cl.A, test_cl.B, test_cl.C, test_cl._X, test_cl.tst4(), test_cl.test_string()]

        self.assertEqual(orig, my_ser)

    def test_json_func(self):
        func = self.json.dumps(rec_func)
        func = self.json.loads(func)

        orig = [rec_func(p) for p in range(34)]
        my_ser = [func(p) for p in range(34)]

        self.assertEqual(orig, my_ser)

    def test_xml_func(self):
        func = self.xml.dumps(rec_func)
        func = self.xml.loads(func)

        orig = [rec_func(i) for i in range(84)]
        my_ser = [func(i) for i in range(84)]

        self.assertEqual(orig, my_ser)

    def test_json_gen(self):
        s_gen = self.json.dumps(gen)
        s_gen = self.json.loads(s_gen)

        orig = [*gen()]
        my_ser = [*s_gen()]

        self.assertEqual(orig, my_ser)

    def test_xml_gen(self):
        s_gen = self.xml.dumps(gen)
        s_gen = self.xml.loads(s_gen)

        orig = [*gen()]
        my_ser = [*s_gen()]

        self.assertEqual(orig, my_ser)

    def test_json_dec(self):
        df = self.json.dumps(decorated_func)
        df = self.json.loads(df)

        orig = [decorated_func(i) for i in range(46)]
        my_ser = [df(i) for i in range(46)]

        self.assertEqual(orig, my_ser)

    def test_xml_dec(self):
        df = self.xml.dumps(decorated_func)
        df = self.xml.loads(df)

        orig = [decorated_func(i) for i in range(26)]
        my_ser = [df(i) for i in range(26)]

        self.assertEqual(orig, my_ser)


if __name__ == '__main__':
    unittest.main()
