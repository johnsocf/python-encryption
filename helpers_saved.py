
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
