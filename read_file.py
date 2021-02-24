import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'test.csv')


def read_file(file_name):
    for row in open(file_name, "r"):
        yield row

for str in read_file(file_name= filename):
    print(str)


def add_numbers(a, b):
	return a + b
