#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    total_value = 0
    if count > 0:
        for i in range(count):
            total_value += int(sys.argv[i + 1])
    print("{}".format(total_value))
