#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        if argc == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(argc))
        for i, arg in enumerate(argv[1:], 1):
            print("{}: {}".format(i, arg))
