# Your names:
#
#
#
#

# Did you copy and paste code from any online source?

# Note: you are not allowed to do so for this assignment.
# Your answer should generally be "no". But if you did,
# mark the code clearly and explain here why you needed to do so.

# Did you collaborate with someone outside your team?
# If yes, explain what you obtained from the collaboration.

# Did you post queries on online forums (such as stackoverflow, ..)
# related to this assignment?
# If yes, post the links here.

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

# -------------------------------------------
import math
# Math is being imported to take the square root of n
# to set a largest possible endpoint to a prime
#factor of n


# This is the brute force algorithm.
# You are being asked to improve upon this
def factorize(n):
    for i in range(3, n-1):
        if n % i == 0:
            return i
    assert False, 'You gave me a prime number to factor'
    return -1


# Improve on factorize function above:
# Call your functions factorize1, factorize2, ...
# Please write a brief comment before each function to describe
# the improvements you are trying out.


# ------------------

# Below are additional helper functions that I (Cat) have added to make my code more modular:

def brute_f_check_for_prime_endpoint_sqrt_num(start, n):
    end_range = int(n ** (1 / 2))
    for i in range(start, end_range):
        if n % i == 0:
            return
    return n

def check_for_primality_descending(start, n):
    end_range = int(n ** (1 / 2))
    for i in range(start, end_range, -1):
        if n % i == 0:
            return
    return n


def check_primality_in_known_set(n, prime_set_basic):
    for i in range(0, len(prime_set_basic)):
        print('i in prime set', prime_set_basic[i])
        if n % prime_set_basic[i] == 0:
            return prime_set_basic[i]
    else:
        return 'now checking remaining set'

def find_primes(start, end):
    prime_list = list(range(start, end))
    return list(filter(is_prime, prime_list))

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return
    return n

# ---------------------

def factorize1(n):
    prime_set_basic1 = [2, 3, 5, 7, 11, 13, 17, 19]
    prime_set_basic1a = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    prime_set_basic2 = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]
    knownPrimes = [prime_set_basic1, prime_set_basic1a, prime_set_basic2]


    for i in range(0, len(knownPrimes)):
        prime_found = check_primality_in_known_set(n, knownPrimes[i])
        if (type(prime_found) is int and prime_found != n):
            return prime_found

    prime_found = brute_f_check_for_prime_endpoint_sqrt_num(139, n)
    if type(prime_found) is int:
        return prime_found
    print('number is determined to be prime')
    return -1

factorize1(10);

def factorize2(n):
    knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]
    prime_found = check_primality_in_known_set(n, knownPrimes)
    if type(prime_found) is int and prime_found != n:
        return prime_found
    prime_found = brute_f_check_for_prime_endpoint_sqrt_num(141, n)
    if type(prime_found) is int and prime_found != n:
        return prime_found
    print('number is determined to be prime')
    return -1
# ...

def factorize3(n):
    knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]
    prime_found = check_primality_in_known_set(n, knownPrimes)
    if type(prime_found) is int and prime_found != n:
        return prime_found
    prime_found = check_for_primality_descending(141, n)
    if type(prime_found) is int and prime_found != n:
        return prime_found
    print('number is determined to be prime')
    return -1
# ...


#def factorize4(n):
# ...

# ...

# Below are additional helper functions that I (Cat) have added to make my code more modular:

def brute_f_check_for_prime_endpoint_sqrt_num(start, n):
    end_range = int(n ** (1 / 2))
    for i in range(start, end_range):
        if n % i == 0:
            return
    return n

def check_for_primality_descending(start, n):
    end_range = int(n ** (1 / 2))
    for i in range(start, end_range, -1):
        if n % i == 0:
            return
    return n


def check_primality_in_known_set(n, prime_set_basic):
    for i in range(0, len(prime_set_basic)):
        print('i in prime set', prime_set_basic[i])
        if n % prime_set_basic[i] == 0:
            return prime_set_basic[i]
    else:
        return 'now checking remaining set'

def find_primes(start, end):
    prime_list = list(range(start, end))
    return list(filter(is_prime, prime_list))

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return
    return n



# Below we have test code:
# to test your function say factorize2, you would simply call

# python3 factorize_main.py factorize2

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
    f = open('composite_list.txt', 'r')
    # print_file = open('digit_list.txt', 'w')
    fun_file = fun.__name__ + '.txt'
    log_file = open(fun_file, 'w')
    # test each number
    digits = {}
    # time = []
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
        print('Factor = ', p, ' other factor = ', n/p, ' Time Elapsed: ', time_elapsed)
        if n % p != 0:
            print('Factorization failed for: ', n)
            sys.exit(1)
    f.close()
    print('digits', digits);
    for length, seconds in digits.items():
        print('length', length)
        print('seconds', seconds)

        log_file.write("%s %f\n" % (length, seconds))

    log_file.close()

