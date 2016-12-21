#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------
import sys

cache = {}
# ------------
# collatz_read
# ------------
def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints
    """
    a = s.split()
    return [int(a[0]), int(a[1])]


def memo(f):
    def func(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return func


@memo
def collatz_seq(n):
    global cache
    seq = [n]
    # assert n > 0
    # if n < 1:
    #     return seq[1]
    while n > 1:
        if (n % 2 == 0):
            n >>= 1
        else:
            n += (n << 1) + 1
        seq.append(n)
    return seq


def collatz_compare(seq1, seq2):
    for i in seq1:
        for j in seq2:
            if j == i:
                return j, seq1.index(j), seq2.index(j)

# -------------
# collatz_print
# -------------
def collatz_print (writer, first, second, value1, value2, common_val) :
    """
    print three ints
    writer a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    writer.write(str(first) + " needs " + str(value1) + " steps, " +
        str(second) + " needs " + str(value2) + " steps, "  +
            "they meet at " + str(common_val) + "\n")


# -------------
# collatz_solve
# -------------
def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        if (i == 0) or (j == 0):
            return
        seq1    = collatz_seq(i)
        seq2    = collatz_seq(j)
        cm, v1, v2     = collatz_compare(seq1, seq2)
        collatz_print(w, i, j, v1, v2, cm)

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)
