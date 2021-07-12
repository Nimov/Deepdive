# Multiline statements & strings section
def string_fun_01():
    a = '''a multi-line string
    that is actually indented in the second line'''
    return a


def string_fun_02():
    a = '''a multi-line string
that is not indented in the second line'''
    return a


# Conditionals
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('--- MULTILINE STRINGS ---')
    print(string_fun_01())
    print(string_fun_02())
    print('\n--- CONDITIONALS ---')
    if_fun_01(15)
    if_fun_02(15)
    if_fun_03(5)
