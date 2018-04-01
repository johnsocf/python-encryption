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


if __name__ == '__main__':
    # First parse command line arguments and figure out which
    # function we want to test
    if len(sys.argv) <= 1:
        fun = factorize
    else:
        fun_to_call_string = sys.argv[1]
        assert fun_to_call_string in globals(), ('You did not implement '+fun_to_call_string)
        globals_copy= globals().copy()
        fun = globals_copy.get(fun_to_call_string)
    # Open the file with list of numbers
    f = open('random_number_for_analysis.txt', 'r')
    # name and start two files for logs for this function's tests
    fun_file = fun.__name__ + '_overall.txt'
    number_fun_file = fun.__name__ + '_numbers.txt'
    log_file = open(fun_file, 'w')
    number_log_file = open(number_fun_file, 'w')
    # number set structures for printing to file
    digits = {}
    number_set = [{value: 0, time: 0}]
    # test each number
    for line in f:
        n = int(line)
        print('Factoring', n, '(', len(line), 'digits ): ', end='')
        t1 = time_clock() # Record time
        p = fun(n)
        t2 = time_clock() # Record time
        time_elapsed = t2 - t1  # seconds
        print('n', n)
        print('p', p)
        if len(line) not in digits:
            digits[len(line)] = time_elapsed
        if digits[len(line)] < time_elapsed:
            digits[len(line)] = time_elapsed
        number_set.append({value: n, time: time_elapsed})
        print('Factor = ', p, ' other factor = ', n/p, ' Time Elapsed: ', time_elapsed)
        if n % p != 0:
            print('Factorization failed for: ', n)
            sys.exit(1)
        # if time elapsed is greater than 5 - print and exit
    f.close()
    print('digits', digits);
    for value, time in number_set.items():
        number_log_file.write("%s %f\n" % (value, time))
    for length, seconds in digits.items():
        print('length', length)
        print('seconds', seconds)
        log_file.write("%s %f\n" % (length, seconds))

    log_file.close()
