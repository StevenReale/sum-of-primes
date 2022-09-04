import math
#sum of all primes less than input
input = 2000000

#initializes variables for main while loop
primelist = [2, 3]
primeTotal = 5
startTest = 4
print("2 is prime")

#attempts to divide test value by all values currently on primelist that are no larger than test divided by the square root of the previously found prime
def isPrime(primelist, test):
    span = len(primelist)
    for i in range(span):
        if primelist[i] > test/math.sqrt(primelist[i]):
            print(test, "is prime")
            return True
        if test % primelist[i] == 0:
            return False

#calls isPrime to determine if value is prime. If it is, it adds it to primelist and to the running sum of primes
while startTest < input:
    if isPrime(primelist, startTest) == True:
        primelist.append(startTest)
        primeTotal += startTest
    startTest += 1

print("The sum of all primes less than", input, "is", primeTotal)
