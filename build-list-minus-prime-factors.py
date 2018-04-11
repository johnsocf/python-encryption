
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

# worked with this to build new list of common primes using Euler Totient
def check_primality_in_known_set_and_some(n, prime_set_basic):
    new_list = []
    for i in range(0, len(prime_set_basic)):
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


# given any num
#
#
# 1 #create two sets...
# 1a. find primes in set of numbers with said upper limit == num
# 1b. determine multiples of those primes in limit built from 1a.
# 1c  build list of numbers to check.
#
# build list
# for numbers between 2 and num
# build list that includes, primes, and numbers that are *not multiples of those primes.
#
# for every new number...
# 2
# 2a # find new primes between upper limit of list 1a. - add these to list 1a.
# 2b determine muliples of all primes in new set 1a for range from last in sorted set 1b to num
# 2c update list
#
# update list
# add new primes found
# add new numbers that are not multiples of primes being assembled in list prime a.
#
# test function
# for any num - for range 2 to closest value in list less than i
#     test to see if numbers are factors of the num.

# determine primes in sequence (only odds...)
# determine multiples in sequence (params for range)


#keep building the next step, the next multiple of prime if it is a prime.
# find number in list, if it's there... skip it. look up prime it is a multiple of, reset to the next multiple of prime.. continue.

import copy



def factorize9(n):
    # initialize variables and flags.
    # start count with two as a prime and a bump up in it's multiple to the next.
    count = {4: 2}
    i = 3;
    log_file = open('list_of_primes_two.txt', 'w')

    # set loop to run untill we reach n
    while i <= n:

        # set local variables.  deep copy count dict for immutability
        condition = True
        count_deep = copy.deepcopy(count)

        for j in count:
            # see if this iteration exists as key in loop
            if i == j:
                # find prime associated with this iteration of the loop
                prime_associated = int(count_deep[i])
                # reset our building dict
                count_deep = {}


                # rebuild the count dict based on count data clone a deep copy
                count_deep = {j: count[j] for j in count if j != i}

                # set sub count to accommodate numbers which have common primes as multiples.
                # we find the next 'bump' of the multiplicative factor of the prime number that is
                # in the series, and if it's not already in our dict object we leave it.  if it is we use the
                # counter to keep track of the multiples and find one that's not yet in our object
                test_count = 1
                while test_count > 0:
                    multiplicative_factor = i + (int(prime_associated) * test_count)
                    test_count = test_count + 1
                    if multiplicative_factor not in count_deep:
                        count_deep[multiplicative_factor] = prime_associated
                        test_count = 0
                        condition = False;
                        break
                # a condition flag allows us to break out of the main iteration and move to the next if we have
                # found i to be a known multiple of a prime tested as a possible factor
                if (not condition):
                    continue
                i = i + 1

        # reassign the rebuilt count object as the count dict
        # by inverse association anything that's not a known multiple of an existing prime is in and
        # of itself prime
        count = count_deep
        if (condition):
            log_file.write("%s\n" % i)
            # print('i prime', i)
            new_key = (i + i)
            count[new_key] = i

        # we iteration one by one to keep precise track of all the known primes and their multiples to find new
        # primes by the inverse, i.e. what is not a multiple.
        i = i + 1

    log_file.close()
    print('false')
    # if no factor is yet found then we know that n is prime.
    return -1



factorize9(2605796209);
