#!/usr/bin/env python3

import curses
import sys
from controls import MandelCLI


def main(stdscr):
    app = MandelCLI(stdscr)
    app.run()


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("\nExiting MandelCLI...")
        sys.exit(0)

