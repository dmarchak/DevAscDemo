import sys

#!/usr/bin/env python3

"""
myscript.py

Basic Python script scaffold.
"""



def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    print("Hello from myscript.py")
    print(f"Received arguments: {argv}")


if __name__ == "__main__":
    main()