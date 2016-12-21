#!/usr/bin/env python3

"""
TestNetflix.py
    Tests Netflix.py for correct functionality
    Unit Testing
"""

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print
from Netflix import netflix_print_summary, netflix_solve, Caches

# -----------
# TestNetflix
# -----------


class TestNetflix(TestCase):

    """
        Tests Netflix.py for correct functionality
        Unit Testing
    """
    # ----
    # read
    # ----

    def test_read_1(self):
        """
            Tests read to see if it reads a movie line correctly
        """
        s_line = "1:\n"
        i, j = netflix_read(s_line)
        self.assertEqual(i, True)
        self.assertEqual(j, 1)

    def test_read_2(self):
        """
            Tests read to see if it reads a customer id correctly
        """
        s_line = "1564536453\n"
        i, j = netflix_read(s_line)
        self.assertEqual(i, False)
        self.assertEqual(j, 1564536453)

    def test_read_3(self):
        """
            Tests read to see if it reads a multidigit movie line correctly
        """
        s_line = "100253:\n"
        i, j = netflix_read(s_line)
        self.assertEqual(i, True)
        self.assertEqual(j, 100253)

    def test_print_1(self):
        """
            Tests print to see if prints a movie line correctly
        """
        writer = StringIO()
        netflix_print(writer, True, 2153330)
        self.assertEqual(writer.getvalue(), "2153330:\n")

    def test_print_2(self):
        """
            Tests print to see if prints a prediction line correctly
        """
        writer = StringIO()
        netflix_print(writer, False, 3.5)
        self.assertEqual(writer.getvalue(), "3.5\n")

    def test_print_3(self):
        """
            Tests print to see if prints a prediction line correctly
        """
        writer = StringIO()
        netflix_print(writer, False, 3.59648694869)
        self.assertEqual(writer.getvalue(), "3.6\n")

    def test_print_summary_1(self):
        """
            Tests print_summary to see if it calculates RMSE and total records
        """
        writer = StringIO()
        cache = Caches(True)
        cache.review_prediction_count = 1
        netflix_print_summary(writer, cache)
        self.assertEqual(writer.getvalue(), "RMSE:0.00\n1 records total\n")

    def test_print_summary_2(self):
        """
            Tests print_summary to see if it calculates RMSE and
            total records with commas
        """
        writer = StringIO()
        cache = Caches(True)
        cache.rmse = 125000
        cache.review_prediction_count = 5000
        netflix_print_summary(writer, cache)
        self.assertEqual(writer.getvalue(), "RMSE:5.00\n5,000 records total\n")

    def test_print_summary_3(self):
        """
            Tests print_summary to see if it calculates RMSE and
            total records with commas
        """
        writer = StringIO()
        cache = Caches(True)
        cache.rmse = 395803456.452523
        cache.review_prediction_count = 2135468
        netflix_print_summary(writer, cache)
        self.assertEqual(
            writer.getvalue(), "RMSE:13.61\n2,135,468 records total\n")

    def test_eval_1(self):
        """
            Tests the predictions of the customer's rating of movie
        """
        cache = Caches(True)
        prediction = netflix_eval(1, 1, cache)
        self.assertEqual(prediction, 4.08)

    def test_eval_2(self):
        """
            Tests the predictions of the customer's rating of movie
            where prediction was less than 1
        """
        cache = Caches(True)
        prediction = netflix_eval(4, 10, cache)
        self.assertEqual(prediction, 1.00)

    def test_eval_3(self):
        """
            Tests the predictions of the customer's rating of movie
            where prediction was greater than 5
        """
        cache = Caches(True)
        prediction = netflix_eval(3, 8, cache)
        self.assertEqual(prediction, 5.00)

    def test_solve_1(self):
        """
            Tests solve using test version
        """
        reader = StringIO("1:\n1\n4\n")
        writer = StringIO()
        netflix_solve(reader, writer, True)
        self.assertEqual(
            writer.getvalue(), "1:\n4.1\n5.0\nRMSE:0.76\n2 records total\n")

    def test_solve_2(self):
        """
            Tests solve using test version
        """
        reader = StringIO("2:\n3\n4\n3:\n1\n3\n4\n")
        writer = StringIO()
        netflix_solve(reader, writer, True)
        self.assertEqual(
            writer.getvalue(),
            "2:\n2.4\n4.4\n3:\n4.1\n5.0\n3.6\nRMSE:0.86\n5 records total\n")

    def test_solve_3(self):
        """
            Tests solve using test version
        """
        reader = StringIO("10:\n4\n")
        writer = StringIO()
        netflix_solve(reader, writer, True)
        self.assertEqual(
            writer.getvalue(), "10:\n1.0\nRMSE:0.00\n1 records total\n")

    # ----
    # caches
    # ----

    def test_caches_init_1(self):
        """
            Tests to see that Caches' review_prediction_count
            value is initialized to 0
        """
        cache = Caches(True)
        self.assertEqual(cache.review_prediction_count, 0)

    def test_caches_init_2(self):
        """
            Tests to see that Caches' rmse value is initialized to 0
        """
        cache = Caches(True)
        self.assertEqual(cache.rmse, 0)

    def test_caches_init_3(self):
        """
            Tests to see that Caches' test version has actual ratings
        """
        cache = Caches(True)
        self.assertEqual(cache.actual_ratings[10][4], 1)
        self.assertEqual(cache.actual_ratings[1][1], 3)

    def test_caches_increment_count_1(self):
        """
            Tests to see that review_prediction_count is incremented by 1
        """
        cache = Caches(True)
        cache.increment_count()
        self.assertEqual(cache.review_prediction_count, 1)

    def test_caches_increment_count_2(self):
        """
            Tests to see that review_prediction_count is incremented by 1
        """
        cache = Caches(True)
        cache.review_prediction_count = 55
        cache.increment_count()
        self.assertEqual(cache.review_prediction_count, 56)

    def test_caches_increment_count_3(self):
        """
            Tests to see that review_prediction_count is incremented by 1
        """
        cache = Caches(True)
        cache.review_prediction_count = -1
        cache.increment_count()
        self.assertEqual(cache.review_prediction_count, 0)

    def test_caches_increment_rmse_1(self):
        """
            Tests to see that rmse is incremented by the value provided
        """
        cache = Caches(True)
        cache.increment_rmse(0.2335785)
        self.assertEqual(cache.rmse, 0.2335785)

    def test_caches_increment_rmse_2(self):
        """
            Tests to see that rmse is incremented by the value provided
        """
        cache = Caches(True)
        cache.rmse = 25
        cache.increment_rmse(-2.6)
        self.assertEqual(cache.rmse, 22.4)

    def test_caches_increment_rmse_3(self):
        """
            Tests to see that rmse is incremented by the value provided
        """
        cache = Caches(True)
        cache.rmse = -1
        cache.increment_rmse(0)
        self.assertEqual(cache.rmse, -1)

# ----
# main
# ----

if __name__ == "__main__":
    main()
