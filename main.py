import random
import string
import os
import sys


class Writer(object):
    def __init__(self, directory='', filename='random', max_files=sys.maxsize,
                 max_file_size=10000000):
        self.ii = 1
        self.directory, self.filename = directory, filename
        self.max_file_size, self.max_files = max_file_size, max_files
        self.finished, self.fh = False, None
        self.open()

    def rotate(self):
        if os.stat(self.filename_template).st_size > self.max_file_size:
            self.close()
            self.ii += 1
            if self.ii <= self.max_files:
                self.open()
            else:
                self.close()
                self.finished = True

    def open(self):
        self.fh = open(self.filename_template, 'w')

    def write(self, text=""):
        self.fh.write(text)
        self.fh.flush()
        self.rotate()

    def close(self):
        self.fh.close()

    @property
    def filename_template(self):
        return self.directory + self.filename + "_%0.2d.txt" % self.ii



def generate_alphabet(size=random.randint(1, 27), chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for i in range(size))


def generate_integer():
    return random.randint(000000000, 999999999)


def generate_real():
    return random.uniform(000000000, 99999999)


def generate_alphanumerics():
    return " " * random.randint(0, 10) + ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=random.randint(0, 36))) + " " * random.randint(0, 10)


if __name__ == '__main__':
    randomfile = Writer(max_files=1)
    buffer = ""
    while not randomfile.finished:
        try:
            buffer += generate_alphabet() + ", " + str(generate_integer()) + ", " + str(generate_real()) + ", " + str(
                generate_alphanumerics()) + ", "

            if len(buffer) >= 100000:
                randomfile.write(buffer)
                buffer = ""
        except ValueError as e:
            randomfile.close()