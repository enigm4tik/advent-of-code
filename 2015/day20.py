import itertools

biggest_prime_used = 0

with open("2015/primenumbers") as file:
    primes = file.readlines()
    primes = [line.rstrip().split(', ') for line in primes]
    primes = [int(line) for line in primes[0]]

def prime_factorization(number, prime_factors=[], end = False):
    if number == 1 or number in primes:
        prime_factors.append(number)
        return prime_factors
    else:
        for prime in primes:
            if number % prime == 0:
                global biggest_prime_used
                if prime > biggest_prime_used:
                    biggest_prime_used = prime
                prime_factors.append(prime)
                return prime_factorization(number//prime, prime_factors[:])
    return prime_factors

counter = { i:0 for i in range(18000)}
permutations = []
present_sum = 0
i = 1

prime_factorization(1)

def getSum(number):
    # print("Number: ", number)
    a = prime_factorization(number, [])
    a.append(1)
    # print(a)
    found_combinations = []
    for j in range(len(a)):
        for x in itertools.combinations(a, j):
            if x:
                found_combinations.append(x)
    results = []
    # print(found_combinations)
    for package in set(found_combinations):
        result = 1
        for p in package:
            result *= p
        results.append(result)
    # print(results)
    mysum = sum(set(results)) * 10
    # print(mysum)
    # print('---')
    return mysum

global badvalues
badvalues = []
global handled
handled = []

def getsum2(number):
    # print("Number: ", number)
    a = prime_factorization(number, [])
    a.append(1)
    # print(a)
    found_combinations = []
    for j in range(len(a)):
        for x in itertools.combinations(a, j):
            if x:
                found_combinations.append(x)
    results = []
    # print(found_combinations)
    for package in set(found_combinations):
        result = 1
        for p in package:
            result *= p
        results.append(result)
    resultset = set(results)
    mysum = 0
    for r in resultset:
        global badvalues
        global handled
        if r in handled:
            continue
        else:
            # print("counted: ", badvalues.count(r))
            if badvalues.count(r) < 50:
                badvalues.append(r)
                mysum += r*11
            else:
                if r not in handled:
                    handled.append(r)
            # print(r)
    return mysum 
    print(mysum)
    print('---')
    return mysum

blasum = 0
i = 1
while blasum < 36000000:
    blasum = getSum(i)
    i += 1
print(i-1)
print(blasum)

# blasum2 = 0
# i = 1
# while blasum2 < 36000000:
#     blasum2 = getsum2(i)
#     i += 1
# print(i-1)
# print(blasum2)
