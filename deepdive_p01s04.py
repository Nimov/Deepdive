from fractions import Fraction
import math
import sys
import time


def calc(a):
    start = time.perf_counter()
    for i in range(10 ** 6):
        a * 2
    end = time.perf_counter()
    return end-start


def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        # which is the same as:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits


def encode(digits, digit_map):
    # we require that digit_map has at least as many
    # characters as the max number in digits
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")

    # we'll see this later, but the following would be better:
    encoding = ''.join([digit_map[d] for d in digits])
    return encoding


def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    # we store the sign of number and make it positive
    # we'll re-insert the sign at the end
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding


def demo():
    print('--- INTEGERS ---')
    print(sys.getsizeof(0))
    print(sys.getsizeof(1))
    print(sys.getsizeof(2 ** 1000))
    print(calc(10))
    print(155 // 4)
    print(155 % 4)
    print(math.floor(155 / 4))
    print(math.floor(-155 / 4))
    print(math.trunc(-155 / 4))
    print(type(10))
    print(int(10.99))
    print(int(True))
    print(int(Fraction(22, 7)))
    print(int("101", 2))
    print(bin(10))
    print(oct(5))
    print(hex(255))
    print(0b0110)
    print(from_base10(10, 2))
    print(from_base10(255, 16))
    print(encode(from_base10(10, 2), "FT"))
    e = rebase_from10(10, 2)
    print(e)
    print(int(e, 2))
    e = rebase_from10(-10, 2)
    print(e)
    print(int(e, 2))
    print('\n--- RATIONAL NUMBERS ---')
    print(Fraction(1))
    print(Fraction(denominator=1, numerator=2))
    print(Fraction(0.125))
    print(Fraction('0.125'))
    print(Fraction('22/7'))
    x = Fraction(2, 3)
    y = Fraction(3, 4)
    print(x+y, x*y, x/y)
    print(x.numerator, y.denominator)
    print(Fraction(math.pi))
    print(Fraction(math.sqrt(2)))
    a = 0.125
    b = 0.3
    print(b.__format__('0.20f'))
    x = Fraction(b)
    print(x)
    print(x.limit_denominator(20))

    return

