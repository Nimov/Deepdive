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
    while start < 10:
        start += 1
        if start % 2:
            continue
        print(start)


def while_fun_05():
    l = [1, 2, 3]
    val = 10

    found = False
    idx = 0
    while idx < len(l):
        if l[idx] == val:
            found = True
            break
        idx += 1

    if not found:
        l.append(val)
    print(l)


def while_fun_06():
    l = [1, 2, 3]
    val = 5
    idx = 0

    while idx < len(l):
        if l[idx] == val:
            break
        idx += 1
    else:
        l.append(val)

    print(l)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('--- MULTILINE STRINGS ---')
    print(string_fun_01())
    print(string_fun_02())
    print('\n--- CONDITIONALS ---')
    if_fun_01(15)
    if_fun_02(15)
    if_fun_03(5)
    print('\n--- FUNCTIONS ---')
    math_fun_01();
    print(math_fun_02(3, 2))
    print(math_fun_02('a', 2))
    print(math_fun_02([1, 2, 3], 2))
    print('\n--- LOOPS ---')
    while_fun_01(4, 10)
    while_fun_02(4, 10)
#   while_fun_03(3)
    while_fun_04(2,9)
    while_fun_05()
    while_fun_06()