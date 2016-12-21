#!/usr/bin/env python3

# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Collatz import collatz_solve

# ----
# main
# ----
if __name__ == "__main__":
    collatz_solve(sys.stdin, sys.stdout)
