import math
import unittest as unit

"""checks if a number "n" is a prime number"""
def is_prime(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True


def test_prime(n,expected):
    assert(is_prime(n)==expected)
