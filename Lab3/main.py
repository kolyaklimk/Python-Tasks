from MySerializer.Factory import Factory, SerializerType

import math


class A:
    def my_method(self):
        return 5


class B:
    def another_method(self):
        return 6


class C(A, B):
    pass


x = 10


def my_func(a):
    return math.sin(x * a)


s = Factory.create_serializer(SerializerType.JSON)
obj = C()
ser_obj = s.dumps(obj)
deser_obj = s.loads(ser_obj)
print(deser_obj.my_method())  # returns 5
print(deser_obj.another_method())  # returns 6

ser_class = s.dumps(C)
deser_class = s.loads(ser_class)
obj = deser_class()
print(obj.my_method())  # returns 5
print(obj.another_method())  # returns 6

ser_func = s.dumps(my_func)
deser_func = s.loads(ser_func)
print(deser_func(20))  # returns sin(10 * 20)
