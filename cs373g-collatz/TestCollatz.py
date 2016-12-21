#/usr/bin/python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cache, cycle_length, collatz_eval_meta_cache, meta_cache

# -----------
# TestCollatz
# -----------
class TestCollatz (TestCase) :
    # ------------
    # cycle_length
    # ------------
    def test_cycle_length_1(self):
        c = cycle_length(1)
        self.assertEqual(c, 1)
    def test_cycle_length_2(self):
        c = cycle_length(7)
        self.assertEqual(c, 17)
    def test_cycle_length_3(self):
        c = cycle_length(11)
        self.assertEqual(c, 15)
    def test_cycle_length_4(self):
        c = cycle_length(14)
        self.assertEqual(c, 18)
    def test_cycle_length_5(self):
        c = cycle_length(1)
        self.assertEqual(c, 1)
    def test_cycle_length_6(self):
        c = cycle_length(3)
        self.assertEqual(c, 8)
    def test_cycle_length_7(self):
        c = cycle_length(5)
        self.assertEqual(c, 6)
    def test_cycle_length_8(self):
        c = cycle_length(9)
        self.assertEqual(c, 20)

    # ----
    # read
    # ----
    def test_read_1(self):
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    def test_read_2(self):
        s    = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)
    def test_read_3(self):
        s    = "100 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 210)
    def test_read_4(self):
        s    = "101 900\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 101)
        self.assertEqual(j, 900)
    def test_read_5(self):
        s    = "900 2000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 900)
        self.assertEqual(j, 2000)
    def test_read_(self):
        s = "9000 2000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 9000)
        self.assertEqual(j, 2000)

    # ----
    # eval
    # ----
    def test_eval_1(self):
        v = collatz_eval(1234, 1234)
        self.assertEqual(v, 133)
    def test_eval_2(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)
    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)
    def test_eval_4(self):
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)
    def test_eval_5(self):
        v = collatz_eval(1, 1000)
        self.assertEqual(v, 179)
    def test_eval_6(self):
        v = collatz_eval(100, 900)
        self.assertEqual(v, 179)
    def test_eval_7(self):
        v = collatz_eval(100, 1000)
        self.assertEqual(v, 179)
    def test_eval_8(self):
        v = collatz_eval(1000, 100)
        self.assertEqual(v, 179)


    def test_eval_meta_cache_1(self):
        v = collatz_eval_meta_cache(1234, 1234)
        self.assertEqual(v, 133)
    def test_eval_meta_cache_2(self):
        v = collatz_eval_meta_cache(1, 1)
        self.assertEqual(v, 1)
    def test_eval_meta_cache_3(self):
        v = collatz_eval_meta_cache(100, 200)
        self.assertEqual(v, 125)
    def test_eval_meta_cache_4(self):
        v = collatz_eval_meta_cache(1, 1000)
        self.assertEqual(v, 179)
    def test_eval_meta_cache_5(self):
        v = collatz_eval_meta_cache(1000, 100)
        self.assertEqual(v, 179)
    def test_eval_meta_cache_6(self):
        v = collatz_eval_meta_cache(1, 1000000)
        self.assertEqual(v, 525)
    def test_eval_meta_cache_7(self):
        v = collatz_eval_meta_cache(40, 100020)
        self.assertEqual(v, 351)
    def test_eval_meta_cache_8(self):
        v = collatz_eval_meta_cache(1002, 4500)
        self.assertEqual(v, 238)


    # -----
    # print
    # -----
    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 100, 210, 125)
        self.assertEqual(w.getvalue(), "100 210 125\n")
    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")
    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 100, 1000, 179)
        self.assertEqual(w.getvalue(), "100 1000 179\n")
    def test_print_5(self):
        w = StringIO()
        collatz_print(w, 1000, 100, 179)
        self.assertEqual(w.getvalue(), "1000 100 179\n")


    # -----
    # solve
    # -----
    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    def test_solve_2(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    def test_solve_3(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n1 999999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n1 999999 525\n")


# ----
# main
# ----
if __name__ == "__main__" :
    main()
