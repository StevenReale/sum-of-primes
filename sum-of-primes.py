#sum of all primes less than input
input = 2000000

#initializes variables for main while loop
primelist = [2]
primeTotal = 2
startTest = 3
print("2 is prime")

#attempts to divide test value by all values currently on primelist
def isPrime(primelist, test):
    span = len(primelist)
    for i in range(span):
        if test % primelist[i] == 0:
            return False
    print(test, "is prime")
    return True

#calls isPrime to determine if value is prime. If it is, it adds it to primelist and to the running sum of primes
while startTest < input:
    if isPrime(primelist, startTest) == True:
        primelist.append(startTest)
        primeTotal += startTest
    startTest += 1

print("The sum of all primes less than", input, "is", primeTotal)
