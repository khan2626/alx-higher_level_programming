#!/usr/bin/python3

if __name__ == "__main__":
    """prints the number and list of argument"""

    import sys

    args = sys.argv
    num_args = len(args) - 1

    print("{} argument".format(num_args))

    if num_args > 0:
        for arg in args[1:]:
            print(arg)
        else:
            print("0 arguments")
    
