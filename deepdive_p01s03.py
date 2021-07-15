import ctypes
import gc
import sys


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
        return "Not found"


class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))


def demo():
    print('--- REFERENCES ---')
    my_var = 10
    print('Hex address of variable a is {0}'.format(hex(id(my_var))))
    a = [1, 2, 3]
    print('Count reference from sys model: {0}'.format(sys.getrefcount(a)))
    print('Count reference from c type: {0}'.format(ref_count(id(a))))
    b = a
    print('Count reference from c type: {0}'.format(ref_count(id(a))))
    b = None
    a_id = id(a)
    a = None
    print('Count reference from c type: {0}'.format(ref_count(a_id)))
    print('\n--- GARBAGE COLLECTOR ---')
    print('GC enabled: {0}'.format(gc.isenabled()))
    gc.disable()
    my_var = A()
    a_id = id(my_var)
    b_id = id(my_var.b)
    print(ref_count(a_id))
    print(ref_count(b_id))
    my_var = None
    print(ref_count(a_id))
    print(ref_count(b_id))
    gc.collect()
    print(ref_count(a_id))
    print(ref_count(b_id))
