import re


def regex(word):
    pattern_alphabet = re.compile("[a-z]+")
    pattern_integer = re.compile("[0-9]+")
    pattern_float = re.compile("[0-9]*.[0-9]+")
    pattern_alphanumeric = re.compile("[0-9a-z]+")

    if pattern_alphabet.fullmatch(word) is not None:
        print('{} {} {}'.format(word, " - ", "alphabetical strings"))
    elif pattern_integer.fullmatch(word) is not None:
        print('{} {} {}'.format(word, " - ", "integer"))
    elif pattern_float.fullmatch(word) is not None:
        print('{} {} {}'.format(word, " - ", "real numbers"))
    elif pattern_alphanumeric.fullmatch(word) is not None:
        print('{} {} {}'.format(word, " - ", "alphanumberic"))


def read(filein):
    with open(filein) as file:
        a = file.read()
        mem = [i.strip() for i in a.split(',')]
        for i in mem:
            regex(i)


read("random_01.txt")