def print_twice(string):
    print(string)
    print(string)

def do_twice(f):
    f('spam')
    f('spam')

def do_four(f):
    do_twice(f)

do_four(print_twice)
