#!/usr/bin/python3

if __name__ == "__main__":
    """prints the sum of all arguments."""
    import sys

    total = 0
    args = len(sys.argv) - 1

    for i in range(args):
        total += int(sys.argv[i + 1])

    print("{}".format(total))
    
