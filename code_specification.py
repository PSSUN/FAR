# All scripts should be written based on python3
# All formats must comply with python PEP-8

# Except for special circumstances,
# it is not allowed to submit a program that does not comply with the format specified by this script.

# All scripts in the FAR are command line based programs,
# so the argparse package must be imported,
# other versions of the package for command line input are not allowed.

import argparse
# Blank line
import otrher_packages

Developer = 'Developer name'

# The naming of functions must be in lowercase, with _ between words as spaces.
def function_1():
    # The naming of variable must be in lowercase, with _ between words as spaces.
    # NOTE: Hump ​​nomenclature is not allowed!
    do_something_1 = 'do_something'


def function_2():
    do_something_2 = 'do_something'


def main():
    parser = argparse.ArgumentParser()
    # dest parameters is necessary, content must be in lowercase
    parser.add_argument('-parameters', dest='parameters', help='Instructions for the parameters must be filled in here')
    args = parser.parse_args()
    function_1()
    function_2()
    print('DONE!')


if __name__ == '__main__':
    main()
