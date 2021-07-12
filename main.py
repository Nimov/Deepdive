# Multiline statements & strings section
def string_fun_01():
    a = '''a multi-line string
    that is actually indented in the second line'''
    return a


def string_fun_02():
    a = '''a multi-line string
that is not indented in the second line'''
    return a


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(string_fun_01())
    print(string_fun_02())