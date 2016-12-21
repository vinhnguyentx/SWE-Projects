#!/usr/bin/env python3

"""
Netflix.py
    reads in a list of movie_ids and customer_ids and
    predicts the customer's rating of the movie
    returns mirrored output replacing customer_ids with the predictions
    appends RSME and total ratings at end of file
"""

# -------
# imports
# -------

import pickle


class Caches(object):

    """
        Encapsulates the caches so they can be accessed
        by both netflix_solve() and netflix_eval()
    """
    customer_averages = dict()
    movie_averages = dict()
    movie_years = dict()
    # total is the average rating of all the movies
    total = 3
    actual_ratings = dict()
    review_prediction_count = 0
    rmse = 0

    def __init__(self, testing):
        """
            initializes the object
        """
        if testing:
            self.customer_averages = {
                1: {1997: 0.08, 1998: 0.08, 1999: 0.08, 2004: 0.08,
                    2005: 0.08, 2015: 0.08, 2016: 0.08},
                2: {1997: -1.92, 1998: -1.92, 1999: -1.92, 2004: -1.92,
                    2005: -1.92, 2015: -1.92, 2016: -1.92},
                3: {1997: 0.08, 1998: 0.08, 1999: 0.08, 2004: 1.08,
                    2005: 1.08, 2015: 2.08, 2016: 2.08},
                4: {1997: 2.08, 1998: -0.92, 1999: 1.75, 2004: -1.92,
                    2005: -0.92, 2015: -0.42, 2016: 1.08}}
            self.movie_averages = {
                1: 1.08, 2: -0.59, 3: 1.08, 4: -1.42, 5: -0.67,
                6: 0.08, 7: 0.08, 8: 1.58, 9: -0.92, 10: -1.92}
            self.movie_years = {1: 1999, 2: 1997, 3: 2015, 4: 1998,
                                5: 2015, 6: 1999, 7: 1999, 8: 2016,
                                9: 2005, 10: 2004}
            # total is the average rating of all the movies
            self.total = 2.92
            self.actual_ratings = {1: {1: 3, 4: 5},
                                   2: {3: 1, 4: 5},
                                   3: {1: 3, 3: 5, 4: 4},
                                   4: {2: 1, 4: 2},
                                   5: {1: 3, 2: 1, 3: 4, 4: 1},
                                   6: {2: 1, 4: 5},
                                   7: {1: 3, 2: 1, 3: 4, 4: 4},
                                   8: {3: 5, 4: 4},
                                   9: {1: 3, 2: 2, 4: 2},
                                   10: {4: 1}}
        else:
            self.customer_averages = pickle.load(
                open('/u/downing/cs/netflix-cs373/cat3238-customer.p', 'rb'))
            self.movie_averages = pickle.load(
                open('/u/downing/cs/netflix-cs373/cat3238-movie.p', 'rb'))
            self.movie_years = pickle.load(
                open('/u/downing/cs/netflix-cs373/cat3238-years.p', 'rb'))
            # total is the average rating of all the movies
            self.total = pickle.load(
                open('/u/downing/cs/netflix-cs373/cat3238-total.p', 'rb'))
            self.actual_ratings = pickle.load(
                open('/u/downing/cs/netflix-cs373/cat3238-actual.p', 'rb'))
        self.review_prediction_count = 0
        self.rmse = 0

    def increment_count(self):
        """
            increments review_prediction_count
        """
        self.review_prediction_count += 1

    def increment_rmse(self, squared_error):
        """
            increments rmse by the squared_error
        """
        self.rmse += squared_error


# ------------
# netflix_read
# ------------


def netflix_read(s_line):
    """
    read a line that is either a movie_id (indicated by containing a :)
        or customer_idif the line contained a movie_id it updates the
        global variable current_movie
    s_line a string
    return a list [boolean, int] with whether the line contained
        a movie_id or not and the int value of the line
    """
    if ":" in s_line:
        current_movie = int(s_line[:-2])
        return [True, current_movie]
    else:
        return [False, int(s_line)]

# ------------
# netflix_eval
# ------------


def netflix_eval(customer_id, movie_id, caches):
    """
    customer_id the id of the customer
    movie_id the id of the movie
    return a float
        the prediction of the customer's rating of the movie
    caches is the object holding the caches
    """

    prediction = caches.movie_averages[movie_id]
    if customer_id in caches.customer_averages:
        customer_average = caches.customer_averages[
            customer_id][caches.movie_years[movie_id]]
        if customer_average is not 0:
            prediction = (caches.movie_averages[
                          movie_id] + customer_average + caches.total)

    if prediction < 1.0:
        prediction = 1.0
    elif prediction > 5.0:
        prediction = 5.0

    caches.increment_rmse(
        (prediction - caches.actual_ratings[movie_id][customer_id]) ** 2)
    caches.increment_count()

    return prediction

# -------------
# netflix_print
# -------------


def netflix_print(write_out, movie, prediction):
    """
    print either an int or formatted float based on whether
        it is a movie or customer prediction
    write_out is an writer
    movie is a boolean
    prediction is a int or float
    """
    # if movie is true, prediction holds the movie ID
    if movie:
        write_out.write(str(prediction) + ":\n")
    # else print out the prediction of the
    # customer's rating of the current movie
    else:
        write_out.write("{:.1f}".format(prediction) + "\n")

# -------------
# netflix_print_summary
# -------------


def netflix_print_summary(write_out, caches):
    """
    prints the summary of the run
    write_out is an writer
    caches is the object holding the caches
    """
    write_out.write("RMSE:" + "{:.2f}".format(
        (caches.rmse / caches.review_prediction_count) ** 0.5) + "\n")
    write_out.write(
        "{:,}".format(caches.review_prediction_count) + " records total" + "\n")


# -------------
# netflix_solve
# -------------


def netflix_solve(read_in, write_out, testing):
    """
    read_in a reader
    write_out a writer
    """
    movie_id = 0
    caches = Caches(testing)

    for s_line in read_in:
        movie, customer_id = netflix_read(s_line)
        if not movie:
            prediction = netflix_eval(customer_id, movie_id, caches)
            netflix_print(write_out, movie, prediction)
        else:
            movie_id = customer_id
            netflix_print(write_out, movie, movie_id)
    netflix_print_summary(write_out, caches)
