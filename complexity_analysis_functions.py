#----------- IMPORTS ---------------------

# If you have import statements, please explain in comments
# why you need them. You can be very brief.

from __future__ import print_function
# I import this just for compatibility with python2 please use python3
# though.

import sys
# sys has useful utilities I need.

from time import clock as time_clock
# Time is being imported to measure
# running time for the factorize
# function.

import math
# Math is being imported to take the square root of n
# to set a largest possible endpoint to a prime
#factor of n

from random import randint
# importing random because I'm needing to generate random digits

# -------------------------------------------


def add_list_for_complexity_analysis():
    log_file = open('random_number_for_analysis.txt', 'w')
    for i in range(5, 20):
        number_of_randoms = math.ceil(10 ** (i / 2))
        for i in range(0, number_of_randoms):
            random = randint(10 ** (i - 1), (10 ** i) - 1);
            log_file.write("%s\n" % random)
    log_file.close()
å