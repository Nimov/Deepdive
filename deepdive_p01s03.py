import ctypes
import gc
import sys
import time
import string


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


def square(a):
    return a ** 2


def cube(a):
    return a ** 3


def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube


def exec_function(fn, n):
    return fn(n)


def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
        if a is b:
            pass


def fun_opti1():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 10
    f = [1, 2] * 5


def membership_test(n, container):
    for i in range(n):
        if 'p' in container:
            pass


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
    gc.enable()
    print('\n--- TYPES & VARIABLES---')
    a = "hello"
    print(type(a))
    a = 10
    print(hex(id(a)))
    print(type(a))
    a = 15
    print(hex(id(a)))   # whoa!
    my_list = [1, 2, 3]
    print(type(my_list))
    print(hex(id(my_list)))
    my_list.append(4)
    print(hex(id(my_list)))
    my_list = my_list + [4]
    print(hex(id(my_list))) # changed address
    t = ([1, 2], [3, 4])
    print(hex(id(t)))
    t[0].append(3)
    print(hex(id(t)))
    print('\n--- OBJECTS ---')
    a = 10
    print(type(a))
    b = int(10)
    print(type(b))
#   help(int)
    c = int('101', base=2)
    print(c)
    print(type(square))
    f = square
    print(f(2))
    f = select_function(1)
    print(f(25))
    print(select_function(2)(3))
    exec_function(cube, 3)
    print('\n--- OPTIMIZATION ---')
    # integers from -5 to 256 are singletons!
    a = 10
    b = int(10)
    c = int('10')
    d = int('1010', 2)
    print(a is b is c is d)
    # string interning
    a1 = 'hello'
    a2 = 'hello'
    print(id(a1), id(a2))
    b1 = '8 hello world, you are cruel'
    b2 = '8 hello world, you are cruel'
    print(id(b1), id(b2)) # no intern possibly (?)
    c1 = sys.intern('hello world')
    c2 = sys.intern('hello world')
    c3 = 'hello world'
    print(id(c1), id(c2), id(c3))
    start = time.perf_counter()
    compare_using_equals(3000000)
    end = time.perf_counter()
    print('equality: ', end-start)
    start = time.perf_counter()
    compare_using_interning(3000000)
    end = time.perf_counter()
    print('identity: ', end-start)
    # looking up constants
    print(fun_opti1.__code__.co_consts)
    char_list = list(string.ascii_letters)
    char_tuple = tuple(string.ascii_letters)
    char_set = set(string.ascii_letters)
    start = time.perf_counter()
    membership_test(10000000, char_list)
    end = time.perf_counter()
    print('list membership: ', end - start)
    start = time.perf_counter()
    membership_test(10000000, char_tuple)
    end = time.perf_counter()
    print('tuple membership: ', end - start)
    start = time.perf_counter()
    membership_test(10000000, char_set)
    end = time.perf_counter()
    print('set membership: ', end-start)
