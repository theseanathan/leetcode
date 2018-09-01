import sys

"""
comparison of two strings if they are the same, use o(1) space
abc \ b is equal to ab
abc \ ca equals abcA

\ b = backspace
\ c = CapsLock
"""


def main(args):
    return string_comparison(args[0], args[1])


def string_comparison(string1, string2):
    string1 = list(string1)

    if not is_valid(string1):
        return False

    for i in range(len(string1)):
        if string1[i] is '\\':
            if string1[i+1] is 'b':
                string1[i+1] = '#'
                string1[i] = '#'
                string1[i-1] = '#'
            elif string1[i+1] is 'c':
                string1[i+2].capitalize()
                string1[i+1] = '#'
                string1[i] = '#'

    string1 = ''.join(string1)
    string1 = string1.replace('#', '')

    return string1 == string2


def is_valid(string):
    if len(string) == 1 and string[0] == '\\':
        return False
    if string[0:2] == '\\b':
        return False
    if string[len(string) - 2: len(string)] == '\\c':
        return False
    return True


if __name__ == "__main__":
    main(sys.argv[1:])
