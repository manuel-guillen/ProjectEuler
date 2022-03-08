'''
ProjectEuler - Problem 1

Multiples of 3 or 5
========================
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

@author: Manuel Guillen
'''
def sum1toN(n):
    """Given a positive integer n, returns the sum of the integers from 1 to n."""
    return n*(n+1)//2

def sumOfMultiples3or5(n, inclusive=True):
    """Given a positive integer n, returns the sum of the integers from 1 to n (excludes n is inclusive is set to False) that are multiples of 3 or 5."""
    n = n if inclusive else n-1
    return 3*sum1toN(n//3) + 5*sum1toN(n//5) - 15*sum1toN(n//15)

if __name__ == '__main__':
    n = 1000
    print(sumOfMultiples3or5(n, inclusive=False))