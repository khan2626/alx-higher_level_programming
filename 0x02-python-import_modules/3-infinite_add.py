#!/usr/bin/python3

if __name__ == "__main__":
    """prints the sum of all arguments."""
    import sys

    sum = 0
    args = len(sys.argv) - 1

    for i in range(args):
        arg = int(sys.argv[i + 1])
        sum += arg
        print("{}".format(sum))
