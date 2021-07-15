from math import sqrt
from math import exp


# MULTILINE STRINGS
def string_fun_01():
    a = '''a multi-line string
    that is actually indented in the second line'''
    return a


def string_fun_02():
    a = '''a multi-line string
that is not indented in the second line'''
    return a


# CONDITIONALS
# If statements can be nested
def if_fun_01(a):
    if a < 5:
        print('a < 5')
    else:
        if a < 10:
            print('5 <= a < 10')
        else:
            print('a >= 10')
    return


# But the elif statement provides far better readability
def if_fun_02(a):
    if a < 5:
        print('a < 5')
    elif a < 10:
        print('5 <= a < 10')
    else:
        print('a >= 10')
    return


def if_fun_03(a):
    res = 'a < 10' if a < 10 else 'a >= 10'
    print(res)


# FUNCTIONS
def math_fun_01():
    print(sqrt(4))
    print(exp(1))


def math_fun_02(a: int, b: int):
    return a * b


# LOOPS
def while_fun_01(start, end):
    while start < end:
        print(start)
        start += 1


def while_fun_02(start, end):
    while True:
        print(start)
        if start >= end:
            break
        start += 1


def while_fun_03(min_length):
    while True:
        name = input('Please enter your name:')
        if len(name) >= min_length and name.isprintable() and name.isalpha():
            break

    print('Hello, {0}'.format(name))


def while_fun_04(start, stop):
    while start < stop:
        start += 1
        if start % 2:
            continue
        print(start)


def while_fun_05():
    lst = [1, 2, 3]
    val = 10

    found = False
    idx = 0
    while idx < len(lst):
        if lst[idx] == val:
            found = True
            break
        idx += 1

    if not found:
        lst.append(val)
    print(lst)


def while_fun_06():
    lst = [1, 2, 3]
    val = 5
    idx = 0

    while idx < len(lst):
        if lst[idx] == val:
            break
        idx += 1
    else:
        lst.append(val)

    print(lst)


# try/except practice
def while_fun_07(a, b):
    while a < 3:
        print('-------------')
        a += 1
        b -= 1
        try:
            res = a / b
        except ZeroDivisionError:
            print('{0}, {1} - division by 0'.format(a, b))
            res = 0
            break
        finally:
            print('{0}, {1} - always executes'.format(a, b))

        print('{0}, {1} - main loop'.format(a, b))
    else:
        print('\n\nno errors were encountered!')
    return res


# for loops practice
def for_fun_basics():
    for i in range(5):
        print(i)
    for x in [1, 2, 3]:
        print(x)
    for x in ('a', 'b', 'c'):
        print(x)
    for x in [(1, 2), (3, 4), (5, 6)]:
        print(x)
    for i, j in [(1, 2), (3, 4), (5, 6)]:
        print(i, j)


def for_fun_break_continue():
    for i in range(5):
        if i == 3:
            continue
        print(i)
    for i in range(5):
        if i == 3:
            break
        print(i)


def for_fun_search():
    for i in range(1, 5):
        print(i)
        if i % 7 == 0:
            print('multiple of 7 found')
            break
    else:
        print('No multiples of 7 encountered')


def for_fun_indexing(s: str):
    for i in range(len(s)):
        print(i, s[i])
    for i, c in enumerate(s):
        print(i, c)


# CLASSES
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * self._height + 2 * self._width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive!')
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive!')
        else:
            self._height = height

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


def demo():
    print('--- MULTILINE STRINGS ---')
    print(string_fun_01())
    print(string_fun_02())
    print('\n--- CONDITIONALS ---')
    if_fun_01(15)
    if_fun_02(15)
    if_fun_03(5)
    print('\n--- FUNCTIONS ---')
    math_fun_01()
    print(math_fun_02(3, 2))
    print(math_fun_02('a', 2))
    print(math_fun_02([1, 2, 3], 2))
    print('\n--- LOOPS ---')
    while_fun_01(4, 10)
    while_fun_02(4, 10)
    #   while_fun_03(3)
    while_fun_04(2, 9)
    while_fun_05()
    while_fun_06()
    while_fun_07(0, 2)
    for_fun_basics()
    for_fun_break_continue()
    for_fun_search()
    for_fun_indexing("Piotr")
    print('\n--- CLASSES ---')
    r1 = Rectangle(10, 20)
    print(str(r1))
    print(repr(r1))
    r2 = Rectangle(10, 20)
    print('{0}'.format(r1 == r2))