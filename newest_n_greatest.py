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

import math
# Math is being imported to take the square root of n
# to set a largest possible endpoint to a prime
#factor of n

# -------------------------------------------


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

def check_primality_in_known_set(n, prime_set_basic):
    # check if number is a composite of any known prime
    for i in range(0, len(prime_set_basic)):
        if n % int(prime_set_basic[i]) == 0:
            return prime_set_basic[i]
    else:
        # if no primes found check remaining set
        return


def brute_f_check_for_prime_endpoint_sqrt_num(start, n):
    end_range = int(math.floor(math.sqrt(n)))

    for i in range(start, end_range):
        if n % i == 0:
            return i
    return

def check_for_primality_descending(start, n):
    end_range = int(math.floor(math.sqrt(n)))
    for i in reversed(range(start, end_range)):
        if n % i == 0:
            return i
    return


def check_for_primality_ascending_eliminate_options_filter(start, n):
    end_range = int(math.floor(math.sqrt(n)))
    i = start
    pattern_set_to_odds = False
    # if number is a perfect square it is composite
    if (end_range**2 == n):
        return end_range
    while i < end_range + 1:

        if n % i == 0:
            print('brute force prime factor is', i)
            return i
        else:
            # set pattern to odds
            # capture known multiples of primes, which would make this composite
            if (not pattern_set_to_odds):
                if i % 2 == 0:
                    i = i + 1
                pattern_set_to_odds = True
            if (i + 2) % 3 == 0:
                i = i + 4
            else:
                i = i + 2
            # if (i + 2) % 3 == 0 or (i + 2) % 5 == 0 or (i + 2) % 7 == 0 or (i + 2) % 11 == 0 or (i + 2) % 13 == 0:
            #     i = i + 4

    return

def check_for_primality_ascending_eliminate_options_simple_filter(start, n):
    end_range = int(math.floor(math.sqrt(n)))
    i = start
    pattern_set_to_odds = False
    # if number is a perfect square it is composite
    if (end_range**2 == n):
        return end_range
    while i < end_range + 1:

        if n % i == 0:
            # print('brute force prime factor is', i)
            return i
        else:
            # capture known multiples of primes, which would make this composite
            if (not pattern_set_to_odds):
                if i % 2 == 0:
                    i = i + 1
                pattern_set_to_odds = True
            i = i + 2
    return

def test_for_digits(n, start):
    end_range = int(math.floor(math.sqrt(n)))
    i = start
    pattern_set_to_odds = False

    # if number is a perfect square it is composite
    if (end_range**2 == n):
        return end_range
    while i < end_range + 1:
        find_acceptable_last_digit = False
        if n % i == 0:
            print('brute force prime factor is', i)
            return i
        else:
            # capture known multiples of primes, which would make this composite
            if (not pattern_set_to_odds):
                if i % 2 == 0:
                    i = i + 1
                pattern_set_to_odds = True
            i = i + 2
        count = 2
        while count > 0:
            sum = i + count
            last_digit = sum % 10
            if last_digit in (1, 3, 7, 9):
                count = 0
                i = i + count
                continue
            else:
                count = count + 2

    return

def test_for_six_num_theory(n, start):
    end_range = int(math.floor(math.sqrt(n)))
    i = start
    miniList = [2, 3]
    # if number is a perfect square it is composite
    if (end_range**2 == n):
        return end_range
    # just test for twos and threes
    for j in range(2, 3+1):
        if n % j == 0:
            return j
    while ((6 * i) + 1) < n:
        test1 = (6 * i) - 1
        test2 = (6 * i) + 1
        if n % test1 == 0:
            print('brute force prime factor is', test1)
            return test1
        if n % test2 == 0:
            print('brute force prime factor is', test2)
            return test2
        i = i + 1
    return



def check_for_primality_descending_eliminate_options_filter(start, n):
    end_range = int(math.floor(math.sqrt(n))) + 1
    i = start
    pattern_set_to_odds = False
    # if number is a perfect square it is composite
    if (end_range**2 == n):
        return end_range

    while end_range > i:
        # capture known multiples of primes, which would make this composite
        if n % end_range == 0:
            return end_range
        else:
            # build pattern for odds
            if (not pattern_set_to_odds):
                if end_range % 2 == 0:
                    end_range = end_range - 1
                else:
                    end_range = end_range - 2
                pattern_set_to_odds = True
            # eliminate loop through obvious composites
            if (end_range - 1) % 3 == 0 or (end_range - 1) % 5 == 0 or (end_range - 1) % 7 == 0 or (end_range - 1) % 11 == 0 or (end_range - 1) % 13 == 0:
                end_range = end_range - 4
            else:

                end_range = end_range - 2
    return

def check_for_primality_descending_eliminate_options_simple_filter(start, n):
    end_range = int(math.floor(math.sqrt(n))) + 1
    i = start
    pattern_set_to_odds = False
    # if number is a perfect square it is composite
    if (end_range**2 == n):
        return end_range
    while end_range > i:
        # eliminate evens
        if n % end_range == 0:
            return end_range
        else:
            # build pattern for odds
            if (not pattern_set_to_odds):
                if end_range % 2 == 0:
                    end_range = end_range - 1
                else:
                    end_range = end_range - 2
                pattern_set_to_odds = True
            else:
                end_range = end_range - 2
    return

# toDo:
# sort list first so that higher than list number primes aren't checked.


# ---------------------


def factorize2(n):
    # assign small set of known primes to array to remove common multiples and filter set to more probable numbers
    knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]

    # check if n is actually in the set
    if n in knownPrimes:
        return n

    # check if n is divisible by a prime in the set and if so return it as a factor.
    prime__factorial_found = check_primality_in_known_set(n, knownPrimes)
    if type(prime__factorial_found) is int and prime__factorial_found != n:
        return prime_found

    # check for prime factor in remaining series, from last prime in list to n
    # return if factor found, otherwise return -1 as n is prime
    prime__factorial_found = check_for_primality_descending(141, n)
    if type(prime__factorial_found) is int and prime__factorial_found != n:
        return prime__factorial_found


    return -1
# ...


def factorize3(n):
    # also remove multiples of primes from set.
    # assign known set to array.
    knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                   103, 107, 109, 113, 127, 131, 137, 139];

    # if n is in this set, it is prime
    if n in knownPrimes:
        return -1

    # check if n is divisible by any prime in the known set.
    # if it is, we have a prime factor found
    prime_found = check_primality_in_known_set(n, knownPrimes)
    if type(prime_found) is int and prime_found != n:
        return prime_found

    # check for prime factor outside of small prime set
    # Filter ooks at numbers in a classic ascending pattern.
    # skips by groups of 4 if number is divisible by common primes.  skips sets faster, not as accurate necessarily
    prime__factorial_found = check_for_primality_ascending_eliminate_options_filter(140, n)

    if type(prime__factorial_found) is int and prime__factorial_found != n:
        return prime__factorial_found
    print('number is determined to be prime')

    return -1

def factorize4(n):

    knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                   103, 107, 109, 113, 127, 131, 137, 139];
    if n in knownPrimes:
        return n

    prime_found = check_primality_in_known_set(n, knownPrimes)
    if type(prime_found) is int and prime_found != n:

        return prime_found

    # much like factorize 3, our filter looks at numbers in a reverse iteration from n descending.
    # skips by groups of 4 if number is divisible by common primes.  skips sets faster, not as accurate necessarily
    prime__factorial_found = check_for_primality_descending_eliminate_options_filter(140, n)
    if type(prime__factorial_found) is int and prime__factorial_found != n:
        return prime__factorial_found
    print('number is determined to be prime')

    return -1

def factorize5(n):

    knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                   103, 107, 109, 113, 127, 131, 137, 139];
    if n in knownPrimes:
        return n

    prime_found = check_primality_in_known_set(n, knownPrimes)
    if type(prime_found) is int and prime_found != n:
        return prime_found

    # simple version of 'factorize4, checks for divisibility in ascending fashion and tests odds  no further jumps in iteration
    prime__factorial_found = check_for_primality_descending_eliminate_options_simple_filter(140, n)
    if type(prime__factorial_found) is int and prime__factorial_found != n:
        return prime__factorial_found
    print('number is determined to be prime')

    return -1

def factorize6(n):
    # also remove multiples of primes from set.

    knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                   103, 107, 109, 113, 127, 131, 137, 139];
    if n in knownPrimes:
        return n

    prime_found = check_primality_in_known_set(n, knownPrimes)
    if type(prime_found) is int and prime_found != n:
        print('factor', prime_found)
        return prime_found

    # simple version of 'factorize3, checks for divisibility in ascending fashion and tests odds  no further jumps in iteration
    prime__factorial_found = check_for_primality_ascending_eliminate_options_simple_filter(140, n)
    # print('prime factor found', prime__factorial_found)
    if type(prime__factorial_found) is int and prime__factorial_found != n:
        return prime__factorial_found
    print('number is determined to be prime')

    return -1



def factorize7(n):
    prime_found = test_for_digits(n, 2)
    if type(prime_found) is int and prime_found != n:
        print('prime found', prime_found)
        return prime_found
    return -1

def factorize8(n):
    prime_found = test_for_six_num_theory(n, 3)
    if type(prime_found) is int and prime_found != n:
        print('prime found', prime_found)
        return prime_found
    return -1

def factorize9(n):
    primes = [3, 5, 7, 11, 13, 17]
    prime_found = check_primality_in_known_set(n, primes)
    if type(prime_found) is int and prime_found != n:
        print('factor', prime_found)
        return prime_found
    end_range = int(math.floor(math.sqrt(n))) + 1
    a = [17 % p for p in primes]
    for i in range(19, end_range):
        for j in range(len(primes)):
            a[j] = (i + 2) % primes[j]
            if all(l != 0 for l in a):
                if n % i == 0:
                    print('factor', i)
                    return i

    if type(prime_found) is int and prime_found != n:
        print('prime found', prime_found)
        return prime_found
    return -1


#prime_found in a lot of places I need to replace with prime__factorial_found
# ...


# ...


# Below we have test code:
# to test your function say factorize2, you would simply call

# python3 factorize_main.py factorize2

if __name__ == '__main__':
    # First parse command line arguments and figure out which
    # function we want to test
    if len(sys.argv) <= 1:
        fun = factorize8
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
        # if time elapsed is greater than 5 - print and exit
        if (n == 72246449675467591861):
            f.close()
            print('digits', digits);
            for length, seconds in digits.items():
                print('length', length)
                print('seconds', seconds)

                log_file.write("%s %f\n" % (length, seconds))

            log_file.close()
    f.close()
    print('digits', digits);
    for length, seconds in digits.items():
        print('length', length)
        print('seconds', seconds)

        log_file.write("%s %f\n" % (length, seconds))

    log_file.close()

