#A function to print all prime factors of a given number x
import math 

def primeFactors(x):

    #Print the number of two's that divide x
    while x % 2 == 0:
        print (2),
        x = x / 2

    # x must be odd at this point
    for i in range (3, int(math.sqrt(x))+1, 2):

        #while i divides x, print i ad divide x
        while x % i == 0:
            print (i), 
            x = x / i

    #condition if x is a prime
    #number greater than 2
    if x > 2:
        print (x)

#Driver Program to test above function
x = 315
primeFactors(x)
