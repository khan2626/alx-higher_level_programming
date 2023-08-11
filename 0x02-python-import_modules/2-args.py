#!/usr/bin/python3

if __name__ == "__main__":
    """prints the number and list of argument"""

    import sys

    args = sys.argv
    num_args = len(args) - 1

    print("{} argument".format(num_args))

    if num_args > 0:
        for i in range(num_args):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))

        else:
            print("0 argument")
            
