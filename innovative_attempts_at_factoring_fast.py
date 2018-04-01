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




# tried mapping out a list minimized from the initial set, so it didn't include multiples of primes
# we don't need to check those.  this was a costly operation, and it crashed my computer
# multiple times by using up too much of the application memory.
# also tried using 'not in' list - if number is not in the list of multiples of primes, then test it
# this too is really costly computationally
def check_for_primality_ascending_eliminate_options(start, n, common_list):
    end_range = int(n ** (1 / 2))
    #new_list = map(minimize_list, range(start, end_range))
    print('NEW LIST', new_list)
    for i in new_list:
        # return if it's a factor of a prime on the common primes list.
        if n % i == 0:
                 return
    return n

# worked with this to build new list of common primes using Euler Totient
def check_primality_in_known_set_and_some(n, prime_set_basic):
    new_list = []
    for i in range(0, len(prime_set_basic)):
        # if n % prime_set_basic[i] == 0 and n != prime_set_basic[i]:
        #     return prime_set_basic[i]
        #if i**2 < n:
            new_list_to_append = eulerTotient(prime_set_basic[i], n)
            new_list = new_list + new_list_to_append
    #else:
    log_file = open('common primes.txt', 'w')
    new_list.sort()
    newest_list = []
    for item in new_list:
        if item not in newest_list:
            newest_list.append(item);
    for newItem in newest_list:
            log_file.write("%s\n" % newItem)

    log_file.close()
    return new_list

# built some test numbers for set of known multiples of primes to build list
# to reduce numbers of searching
def eulerTotient(i, n):
    multiple_of_primes = []
    j = 2
    #while (j * i) < n:
    while j < 51:
        k = j * i
        multiple_of_primes.insert(0, k)
        j = j + 1
    return multiple_of_primes

# sort list first so that higher than list number primes aren't checked.


def get_common_prime_list():
    common_primes = []

    with open('common primes.txt', 'r') as ins:
        ins.readline()
        for line in ins:
            common_primes.append(line.rstrip('\n'))
    return common_primes


# ---------------------

# testing matrix approach.
# can we use matrices to speed this up somehow
def factorize1(n):
    prime_set_basic1 = [2, 3, 5, 7, 11, 13, 17, 19]
    prime_set_basic1a = [23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    prime_set_basic2 = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]
    knownPrimes = [prime_set_basic1, prime_set_basic1a, prime_set_basic2]


    for i in range(0, len(knownPrimes)):
        prime_found = check_primality_in_known_set(n, knownPrimes[i])
        if (type(prime_found) is int and prime_found != n):
            return prime_found

    prime_found = brute_f_check_for_prime_endpoint_sqrt_num(141, n)
    if (type(prime_found) is int and prime_found != n):
        return prime_found
    print('number is determined to be prime')
    return -1





# built and tried to utilize a common prime list
# so that in our check for factors we could eliminate numbers that are on the list
def factorize4(n):
    # also remove multiples of primes from set.
    knownPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                   103, 107, 109, 113, 127, 131, 137, 139];
    if n in knownPrimes:
        return n

    common_primes = get_common_prime_list()
    if n in common_primes:
        return n
    prime_found = check_for_primality_ascending_eliminate_options(141, n, knownPrimes)
    if type(prime_found) is int and prime_found != n:
        return prime_found
    print('number is determined to be prime')

    return -1
