#!/usr/bin/env python
import sys

from pystory import run_pystory

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    run_pystory(args)


if __name__ == "__main__":
    main()
