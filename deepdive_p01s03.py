import ctypes
import sys


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


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