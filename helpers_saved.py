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

# def find_primes(start, end):
#     prime_list = list(range(start, end))
#     return list(filter(is_prime, prime_list))
#
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return
#     return n

# def get_common_prime_list():
#     common_primes = []
#
#     with open('common primes.txt', 'r') as ins:
#         ins.readline()
#         for line in ins:
#             common_primes.append(line.rstrip('\n'))
#     return common_primes
# def test_for_prime_brute(i, n):
#     # test number by number
#     if n % i == 0:
#         return
#     return i

