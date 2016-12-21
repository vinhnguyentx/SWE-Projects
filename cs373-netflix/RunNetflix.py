#!/usr/bin/env python3
"""
	RunNetflix.py
		Runs Netflix.py outside of test mode
"""
# -------
# imports
# -------

import sys

from Netflix import netflix_solve

# ----
# main
# ----
if __name__ == "__main__":
    netflix_solve(sys.stdin, sys.stdout, False)
